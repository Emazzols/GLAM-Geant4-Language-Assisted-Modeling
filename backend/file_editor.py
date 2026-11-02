from pathlib import Path
from .paths import MARKER_TO_FILE


class MarkerNotFoundError(RuntimeError):
    pass


class MarkerBlockMalformedError(RuntimeError):
    pass


def replace_marker_block(marker: str, new_code: str) -> None:
    """
    Substitution of the content between:
      // <MARKER_BEGIN>
      ...
      // <MARKER_END>
    """

    if marker not in MARKER_TO_FILE:
        raise ValueError(f"Unknown marker: {marker}")

    file_path: Path = MARKER_TO_FILE[marker]

    text = file_path.read_text()

    begin = f"// <{marker}_BEGIN>"
    end   = f"// <{marker}_END>"

    begin_idx = text.find(begin)
    end_idx   = text.find(end)

    if begin_idx == -1 or end_idx == -1:
        raise MarkerNotFoundError(
            f"Marker {marker} not found in {file_path}"
        )

    if end_idx < begin_idx:
        raise MarkerBlockMalformedError(
            f"Malformed marker block for {marker} in {file_path}"
        )

    # posizione dopo la riga BEGIN
    begin_line_end = text.find("\n", begin_idx) + 1

    # preserva indentazione
    indent = _extract_indent(text, begin_idx)

    formatted_code = ""
    if new_code.strip():
        formatted_code = "\n".join(
            indent + line if line.strip() else line
            for line in new_code.splitlines()
        ) + "\n"

    new_text = (
        text[:begin_line_end]
        + formatted_code
        + text[end_idx:]
    )

    file_path.write_text(new_text)


def _extract_indent(text: str, idx: int) -> str:
    """
    Estrae l'indentazione della riga che contiene il marker BEGIN
    """
    line_start = text.rfind("\n", 0, idx) + 1
    line = text[line_start:idx]
    return line[:len(line) - len(line.lstrip())]
