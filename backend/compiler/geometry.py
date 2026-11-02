from backend.ir.units import length, vector3, direction3


# =====================================================
# Helpers
# =====================================================

def emit_rotation(rot_dict, name_suffix):
    """
    Generates a G4RotationMatrix only if rotation is defined.
    Returns (var_name, code_string) or (None, None).
    """
    if not rot_dict:
        return None, None

    var = f"rot_{name_suffix}"
    lines = [f"auto {var} = new G4RotationMatrix();"]

    for axis, angle in rot_dict.items():
        lines.append(f"{var}->rotate{axis.upper()}({angle} * deg);")

    return var, "\n".join(lines)


def topo_sort_booleans(boolean_defs):
    """
    boolean_defs: dict[name] = solid_dict
    Returns a list of boolean names in valid construction order
    """

    deps = {
        name: {solid["solid_a"], solid["solid_b"]}
        for name, solid in boolean_defs.items()
    }

    visited = set()
    order = []

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        for d in deps[n]:
            if d in boolean_defs:
                dfs(d)
        order.append(n)

    for name in boolean_defs:
        dfs(name)

    return order


# =====================================================
# Geometry compiler
# =====================================================

def compile_geometry(geometry: dict) -> str:
    lines = []
    lines.append("// --- Geometry generated from IR ---")

    # -------------------------------------------------
    # Primitives
    # -------------------------------------------------

    for kind, items in geometry.get("primitives", {}).items():
        for obj in items:
            name = obj["name"]
            mat = f'nist->FindOrBuildMaterial("{obj["material"]}")'

            if kind == "box":
                hx, hy, hz = obj["half_size"]
                lines.append(
                    f'auto {name} = BuildBox("{name}", '
                    f'G4ThreeVector({length(hx)}, {length(hy)}, {length(hz)}), '
                    f'{mat});'
                )

            elif kind == "cylinder":
                lines.append(
                    f'auto {name} = BuildCylinder("{name}", '
                    f'{length(obj["r_min"])}, '
                    f'{length(obj["r_max"])}, '
                    f'{length(obj["half_height"])}, '
                    f'{mat});'
                )

            elif kind == "sphere":
                lines.append(
                    f'auto {name} = BuildSphere("{name}", '
                    f'{length(obj["radius"])}, '
                    f'{mat});'
                )

            elif kind == "cone":
                lines.append(
                    f'auto {name} = BuildCone("{name}", '
                    f'{length(obj["r_min_bottom"])}, '
                    f'{length(obj["r_max_bottom"])}, '
                    f'{length(obj["r_min_top"])}, '
                    f'{length(obj["r_max_top"])}, '
                    f'{length(obj["half_height"])}, '
                    f'{mat});'
                )

    # -------------------------------------------------
    # Boolean solids (topological order)
    # -------------------------------------------------

    boolean_defs = {}
    for kind, items in geometry.get("boolean", {}).items():
        for obj in items:
            obj["_kind"] = kind
            boolean_defs[obj["name"]] = obj

    order = topo_sort_booleans(boolean_defs)

    for name in order:
        obj = boolean_defs[name]
        kind = obj["_kind"]

        a = obj["solid_a"]
        b = obj["solid_b"]
        mat = f'nist->FindOrBuildMaterial("{obj["material"]}")'

        tr = obj.get("transform", {})
        pos = vector3(tr.get("translation", [
            {"value": 0, "unit": "mm"},
            {"value": 0, "unit": "mm"},
            {"value": 0, "unit": "mm"},
        ]))

        rot_var, rot_code = emit_rotation(tr.get("rotation"), name)

        if rot_code:
            lines.append(rot_code)
            lines.append(f'G4Transform3D tr_{name}(*{rot_var}, {pos});')
        else:
            lines.append(f'G4Transform3D tr_{name}(G4RotationMatrix(), {pos});')

        fn = {
            "union": "BuildUnion",
            "subtraction": "BuildSubtraction",
            "intersection": "BuildIntersection",
        }[kind]

        lines.append(
            f'auto {name} = {fn}("{name}", '
            f'{a}->GetSolid(), '
            f'{b}->GetSolid(), '
            f'tr_{name}, '
            f'{mat});'
        )

    # -------------------------------------------------
    # Placement
    # -------------------------------------------------

    for i, plc in enumerate(geometry.get("placement", [])):
        if plc["type"] == "place":
            child = plc["child"]
            mother = plc["mother"]
            pos = vector3(plc["position"])
            name = plc["name"]
            copy_no = plc.get("copy_no", 0)

            rot_var, rot_code = emit_rotation(plc.get("rotation"), f"{name}_{i}")

            if rot_code:
                lines.append(rot_code)
                rot_expr = rot_var
            else:
                rot_expr = "nullptr"

            lines.append(
                f'Place({child}, {mother}, {pos}, {rot_expr}, "{name}", {copy_no});'
            )

        elif plc["type"] == "stacked":
            vec = f"stack_{i}"
            vols = plc["volumes"]
            mother = plc["mother"]
            axis = direction3(plc["axis"])
            spacing = length(plc["spacing"])

            lines.append(
                f'std::vector<G4LogicalVolume*> {vec} = {{ '
                + ", ".join(vols) +
                ' };'
            )

            lines.append(
                f'PlaceStacked({vec}, {mother}, {axis}, {spacing});'
            )

    return "\n".join(lines)
