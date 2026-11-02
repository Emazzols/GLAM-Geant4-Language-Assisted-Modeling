from backend.compiler.geometry import compile_geometry
from backend.compiler.source import compile_source
from backend.compiler.scoring import compile_scoring
from backend.file_editor import replace_marker_block

def compile_ir(ir: dict) -> None:
    if not isinstance(ir, dict):
        raise TypeError("IR must be a dictionary")

    # IR is assumed VALIDATED upstream
    geom_code = compile_geometry(ir["geometry"])
    src_code = compile_source(ir["source"])
    scoring_code = compile_scoring(ir["scoring"])

    replace_marker_block(
        "INSTRUCTOR_GEOMETRY",
        geom_code,
    )

    replace_marker_block(
        "INSTRUCTOR_SOURCE",
        src_code,
    )

    replace_marker_block(
        "INSTRUCTOR_SCORING",
        scoring_code,
    )
