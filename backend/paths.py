from pathlib import Path

# =====================================================
# Project root
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# =====================================================
# Geant4 project structure
# =====================================================

SIM_DIR = PROJECT_ROOT / "sim"

SIM_SRC = SIM_DIR / "src"
SIM_INCLUDE = SIM_DIR / "include"
SIM_BUILD = SIM_DIR / "build"

# =====================================================
# Executables & runtime files
# =====================================================

EXECUTABLE = SIM_BUILD / "SimpleSim"
RUN_MAC = SIM_BUILD / "run.mac"
SIM_NAME_FILE = SIM_BUILD / "sim_name.txt"

# =====================================================
# Geant4 source files (editable by instructor)
# =====================================================

ACTION_INIT_FILE = SIM_SRC / "ActionInitialization.cc"
PRIMARY_GEN_FILE = SIM_SRC / "PrimaryGeneratorAction.cc"
DETECTOR_CONSTRUCTION_FILE = SIM_SRC / "DetectorConstruction.cc"


# =====================================================
# Semantic aliases (compiler-facing API)
# =====================================================

DETECTOR_CONSTRUCTION = DETECTOR_CONSTRUCTION_FILE
ACTION_INITIALIZATION = ACTION_INIT_FILE

# =====================================================
# Marker → file mapping
# =====================================================

MARKER_TO_FILE = {
    # Scoring
    "INSTRUCTOR_SCORING": ACTION_INIT_FILE,

    # Source configuration
    "INSTRUCTOR_SOURCE": ACTION_INIT_FILE,

    # Geometry definition
    "INSTRUCTOR_GEOMETRY": DETECTOR_CONSTRUCTION_FILE,
}