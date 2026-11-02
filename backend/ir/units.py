"""
Unit handling for Geant4 IR.

This module converts IR quantities into
C++ Geant4 expressions using CLHEP units.
"""

# =====================================================
# Supported units
# =====================================================

LENGTH_UNITS = {"nm", "um", "mm", "cm", "m"}
ENERGY_UNITS = {"eV", "keV", "MeV", "GeV"}

# =====================================================
# Quantity conversion
# =====================================================

def length(q: dict) -> str:
    """
    Convert a length quantity to C++ code.
    Example: {value: 5, unit: 'cm'} -> '5 * cm'
    """
    _check_quantity(q, LENGTH_UNITS)
    return f"{q['value']} * {q['unit']}"


def energy(q: dict) -> str:
    """
    Convert an energy quantity to C++ code.
    Example: {value: 1, unit: 'MeV'} -> '1 * MeV'
    """
    _check_quantity(q, ENERGY_UNITS)
    return f"{q['value']} * {q['unit']}"


def vector3(v) -> str:
    """
    Convert a vector of 3 length quantities to G4ThreeVector.
    """
    if not isinstance(v, (list, tuple)) or len(v) != 3:
        raise ValueError("Vector3 must have exactly 3 components")

    x = length(v[0])
    y = length(v[1])
    z = length(v[2])

    return f"G4ThreeVector({x}, {y}, {z})"

def direction3(vec):
    if not isinstance(vec, (list, tuple)) or len(vec) != 3:
        raise ValueError("Direction must have 3 components")

    for comp in vec:
        if not isinstance(comp, (int, float)):
            raise ValueError("Direction components must be numeric")

    return f"G4ThreeVector({vec[0]}, {vec[1]}, {vec[2]})"


# =====================================================
# Internal helpers
# =====================================================

def _check_quantity(q: dict, allowed_units: set):
    if not isinstance(q, dict):
        raise ValueError("Quantity must be a dict")

    if "value" not in q or "unit" not in q:
        raise ValueError("Quantity must have 'value' and 'unit'")

    if not isinstance(q["value"], (int, float)):
        raise ValueError("Quantity value must be numeric")

    if q["unit"] not in allowed_units:
        raise ValueError(f"Unsupported unit '{q['unit']}'")
