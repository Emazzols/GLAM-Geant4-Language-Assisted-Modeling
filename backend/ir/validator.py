"""
Validator for Geant4 Intermediate Representation (IR).

Responsibilities:
- structural validation against schema.py
- semantic validation against backend capabilities
- unit validation via units.py

NO code generation happens here.
"""

from .schema import (
    GEOMETRY_PRIMITIVES,
    GEOMETRY_BOOLEAN,
    PLACEMENT_TYPES,
    SOURCE_TYPES,
    SOURCE_COMMON_FIELDS,
    SOURCE_TYPE_REQUIRED_FIELDS,
    SOURCE_TYPE_FORBIDDEN_FIELDS,
    SOURCE_DIRECTION_RULES,
)

from .units import (
    ENERGY_UNITS,
    LENGTH_UNITS,
)


# =====================================================
# Errors
# =====================================================

class ValidationError(Exception):
    pass


# =====================================================
# Entry point
# =====================================================

def validate_ir(ir: dict) -> None:
    if not isinstance(ir, dict):
        raise ValidationError("IR must be a dictionary")

    for section in ("geometry", "source", "scoring"):
        if section not in ir:
            raise ValidationError(f"Missing IR section: '{section}'")

    validate_geometry(ir["geometry"])
    validate_source(ir["source"])
    validate_scoring(ir["scoring"], ir["geometry"])


# =====================================================
# Geometry validation
# =====================================================

def validate_geometry(geometry: dict) -> None:
    if not isinstance(geometry, dict):
        raise ValidationError("Geometry section must be a dictionary")

    # -------------------------------------------------
    # Collect primitive solids
    # -------------------------------------------------

    primitives = geometry.get("primitives", {})
    if not isinstance(primitives, dict):
        raise ValidationError("'geometry.primitives' must be a dictionary")

    primitive_names: set[str] = set()

    for prim_type, prim_list in primitives.items():
        if prim_type not in GEOMETRY_PRIMITIVES:
            raise ValidationError(f"Unknown geometry primitive '{prim_type}'")

        if not isinstance(prim_list, list):
            raise ValidationError(f"Primitive '{prim_type}' must be a list")

        required_fields = GEOMETRY_PRIMITIVES[prim_type]["required"]

        for prim in prim_list:
            if not isinstance(prim, dict):
                raise ValidationError("Primitive entry must be a dictionary")

            name = prim.get("name")
            if not name:
                raise ValidationError("Primitive missing 'name'")

            if name in primitive_names:
                raise ValidationError(f"Duplicate volume name '{name}'")

            primitive_names.add(name)

            for field in required_fields:
                if field not in prim:
                    raise ValidationError(
                        f"Primitive '{name}' missing required field '{field}'"
                    )

            validate_material(prim["material"])

    # -------------------------------------------------
    # Collect boolean solids (no order assumptions!)
    # -------------------------------------------------

    booleans = geometry.get("booleans", {})
    if not isinstance(booleans, dict):
        raise ValidationError("'geometry.booleans' must be a dictionary")

    boolean_defs = {}
    boolean_deps = {}

    for bool_type, solid_list in booleans.items():
        if bool_type not in GEOMETRY_BOOLEAN:
            raise ValidationError(f"Unknown boolean solid '{bool_type}'")

        if not isinstance(solid_list, list):
            raise ValidationError(f"Boolean '{bool_type}' must be a list")

        required_fields = GEOMETRY_BOOLEAN[bool_type]["required"]

        for solid in solid_list:
            if not isinstance(solid, dict):
                raise ValidationError("Boolean solid must be a dictionary")

            name = solid.get("name")
            if not name:
                raise ValidationError("Boolean solid missing 'name'")

            if name in primitive_names or name in boolean_defs:
                raise ValidationError(f"Duplicate volume name '{name}'")

            for field in required_fields:
                if field not in solid:
                    raise ValidationError(
                        f"Boolean solid '{name}' missing field '{field}'"
                    )

            validate_material(solid["material"])

            a = solid["solid_a"]
            b = solid["solid_b"]

            boolean_defs[name] = solid
            boolean_deps[name] = {a, b}

    # -------------------------------------------------
    # Validate boolean dependencies
    # -------------------------------------------------

    all_solids = primitive_names | set(boolean_defs.keys())

    for name, deps in boolean_deps.items():
        for d in deps:
            if d not in all_solids:
                raise ValidationError(
                    f"Boolean solid '{name}' references unknown solid '{d}'"
                )

    # -------------------------------------------------
    # Detect cycles in boolean dependency graph
    # -------------------------------------------------

    _check_no_cycles(boolean_deps)

    # -------------------------------------------------
    # Placement validation
    # -------------------------------------------------

    placements = geometry.get("placement", [])
    if not isinstance(placements, list):
        raise ValidationError("'geometry.placement' must be a list")

    for p in placements:
        if not isinstance(p, dict):
            raise ValidationError("Placement entry must be a dictionary")

        place_type = p.get("type")
        if place_type not in PLACEMENT_TYPES:
            raise ValidationError(f"Unknown placement type '{place_type}'")

        spec = PLACEMENT_TYPES[place_type]

        for field in spec["required"]:
            if field not in p:
                raise ValidationError(
                    f"Placement '{place_type}' missing required field '{field}'"
                )

        for field in spec.get("forbidden", set()):
            if field in p:
                raise ValidationError(
                    f"Field '{field}' not allowed in placement type '{place_type}'"
                )

        if place_type == "place":
            if p["child"] not in all_solids:
                raise ValidationError(
                    f"Placement refers to unknown child volume '{p['child']}'"
                )

            if p["mother"] != "worldLV" and p["mother"] not in all_solids:
                raise ValidationError(
                    f"Placement refers to unknown mother volume '{p['mother']}'"
                )

            validate_vector(p["position"])

        elif place_type == "stacked":
            for v in p["volumes"]:
                if v not in all_solids:
                    raise ValidationError(
                        f"Stacked placement refers to unknown volume '{v}'"
                    )

            if p["mother"] != "worldLV" and p["mother"] not in all_solids:
                raise ValidationError(
                    f"Stacked placement refers to unknown mother '{p['mother']}'"
                )

            validate_direction(p["axis"])
            validate_length(p["spacing"])


# =====================================================
# Cycle detection
# =====================================================

def _check_no_cycles(graph: dict[str, set[str]]) -> None:
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            raise ValidationError(
                f"Cyclic boolean dependency detected involving '{node}'"
            )
        if node in visited:
            return

        visited.add(node)
        stack.add(node)

        for dep in graph.get(node, []):
            if dep in graph:  # only follow boolean → boolean edges
                dfs(dep)

        stack.remove(node)

    for node in graph:
        dfs(node)


# =====================================================
# Source validation
# =====================================================

def validate_source(source: dict) -> None:
    if not isinstance(source, dict):
        raise ValidationError("Source must be a dictionary")

    missing = SOURCE_COMMON_FIELDS - source.keys()
    if missing:
        raise ValidationError(f"Source missing fields: {missing}")

    src_type = source["type"]
    if src_type not in SOURCE_TYPES:
        raise ValidationError(f"Invalid source type '{src_type}'")

    for field in SOURCE_TYPE_REQUIRED_FIELDS[src_type]:
        if field not in source:
            raise ValidationError(
                f"Source type '{src_type}' requires '{field}'"
            )

    for field in SOURCE_TYPE_FORBIDDEN_FIELDS[src_type]:
        if field in source:
            raise ValidationError(
                f"Field '{field}' not allowed for source type '{src_type}'"
            )

    exclusive = SOURCE_DIRECTION_RULES["exclusive"]
    present = exclusive & source.keys()

    if len(present) != 1:
        raise ValidationError(
            "Source must specify exactly one of 'direction' or 'isotropic'"
        )
        
    if "direction" in source:
        validate_direction(source["direction"])


    validate_energy(source["energy"])
    validate_vector(source["position"])


# =====================================================
# Scoring validation (unchanged)
# =====================================================

def validate_scoring(scoring: list, geometry: dict):
    if not isinstance(scoring, list):
        raise ValidationError("Scoring section must be a list")

    if not scoring:
        raise ValidationError("Scoring list cannot be empty")

    if len(scoring) != len(set(scoring)):
        raise ValidationError("Scoring volumes must be unique")

    defined = set()

    for prims in geometry.get("primitives", {}).values():
        for p in prims:
            defined.add(p["name"])

    for solids in geometry.get("booleans", {}).values():
        for s in solids:
            defined.add(s["name"])

    for v in scoring:
        if v not in defined:
            raise ValidationError(
                f"Scoring refers to unknown volume '{v}'"
            )


# =====================================================
# Helpers
# =====================================================

def validate_material(material) -> None:
    if not isinstance(material, str):
        raise ValidationError("Material must be a string")


def validate_energy(energy: dict) -> None:
    if "unit" not in energy or energy["unit"] not in ENERGY_UNITS:
        raise ValidationError(f"Invalid energy unit '{energy.get('unit')}'")


def validate_vector(vec) -> None:
    if not isinstance(vec, (list, tuple)) or len(vec) != 3:
        raise ValidationError("Vector must have exactly 3 components")

    for comp in vec:
        if comp.get("unit") not in LENGTH_UNITS:
            raise ValidationError(
                f"Invalid length unit '{comp.get('unit')}'"
            )

def validate_direction(vec):
    if not isinstance(vec, list) or len(vec) != 3:
        raise ValidationError("Direction must be a list of 3 numbers")

    for comp in vec:
        if not isinstance(comp, (int, float)):
            raise ValidationError("Direction components must be numeric")


def validate_length(q: dict) -> None:
    if q.get("unit") not in LENGTH_UNITS:
        raise ValidationError(f"Invalid length unit '{q.get('unit')}'")
    
def validate_direction(d):
    if not isinstance(d, (list, tuple)) or len(d) != 3:
        raise ValidationError("Direction must be a 3-component vector")
    for x in d:
        if not isinstance(x, (int, float)):
            raise ValidationError("Direction components must be numeric")
    if d[0] == 0 and d[1] == 0 and d[2] == 0:
        raise ValidationError("Direction vector cannot be zero")
