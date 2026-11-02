"""
IR schema for Geant4 LLM-safe control system.
Executable semantic schema (used by validator).
"""

# =====================================================
# Units
# =====================================================

LENGTH_UNITS = {"nm", "um", "mm", "cm", "m"}
ENERGY_UNITS = {"eV", "keV", "MeV", "GeV"}

# =====================================================
# Geometry – primitives
# =====================================================

# Primitive solids define named G4LogicalVolume objects.
GEOMETRY_PRIMITIVES = {
    "box": {
        "required": {"name", "half_size", "material"}
    },
    "cylinder": {
        "required": {"name", "r_min", "r_max", "half_height", "material"}
    },
    "sphere": {
        "required": {"name", "radius", "material"}
    },
    "cone": {
        "required": {
            "name",
            "r_min_bottom",
            "r_max_bottom",
            "r_min_top",
            "r_max_top",
            "half_height",
            "material"
        }
    }
}

# =====================================================
# Geometry – boolean solids
# =====================================================

# Boolean solids ALSO define named solids.
# solid_a and solid_b may refer to ANY previously defined solid
# (primitive OR boolean).
GEOMETRY_BOOLEAN = {
    "union": {
        "required": {"name", "solid_a", "solid_b", "transform", "material"}
    },
    "subtraction": {
        "required": {"name", "solid_a", "solid_b", "transform", "material"}
    },
    "intersection": {
        "required": {"name", "solid_a", "solid_b", "transform", "material"}
    }
}

# =====================================================
# Geometry – placement
# =====================================================
# Placement operates on logical volumes, regardless of how they were created.
# Placement order is significant and must be preserved.

PLACEMENT_TYPES = {
    "place": {
        "required": {
            "type",
            "child",
            "mother",
            "position",
            "name",
        },
        "optional": {
            "rotation",
            "copy_no",
        },
        "forbidden": {
            "volumes",
            "axis",
            "spacing",
        },
    },
    "stacked": {
        "required": {
            "type",
            "volumes",
            "mother",
            "axis",
            "spacing",
        },
        "optional": set(),
        "forbidden": {
            "child",
            "position",
            "rotation",
            "name",
            "copy_no",
        },
    },
}

# =====================================================
# Source
# =====================================================

SOURCE_TYPES = {"point", "disk", "sphere"}

SOURCE_COMMON_FIELDS = {
    "particle",
    "energy",
    "type",
    "position",
}

SOURCE_TYPE_REQUIRED_FIELDS = {
    "point": set(),
    "disk": {"radius"},
    "sphere": {"radius"},
}

SOURCE_TYPE_FORBIDDEN_FIELDS = {
    "point": set(),
    "disk": set(),
    "sphere": set(),
}

# Exactly one of these must be present
SOURCE_DIRECTION_RULES = {
    "exclusive": {"direction", "isotropic"}
}

# =====================================================
# Scoring
# =====================================================

SCORING_CONSTRAINTS = {
    "non_empty": True,
    "unique": True,
}
