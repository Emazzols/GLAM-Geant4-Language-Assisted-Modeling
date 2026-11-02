from pathlib import Path
import json

# ============================================================
# PROJECT PATHS
# ============================================================

# This file is located in:
# Geant4LLM/backend/knowledge_base.py

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent
EXAMPLES_DIR = PROJECT_ROOT / "examples"

# ============================================================
# KNOWLEDGE BASE LOADER
# ============================================================

def read_text_file(path):
    """Read a UTF-8 text file."""
    return path.read_text(encoding="utf-8")


def read_json_file(path):
    """Read and parse a JSON file."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_instruction_files(examples_dir):
    """
    Load all files contained directly in examples/instruction/.
    """
    instruction_dir = examples_dir / "instruction"

    instructions = {}

    for path in sorted(instruction_dir.iterdir()):
        if path.is_file():
            if path.suffix.lower() == ".md":
                instructions[path.name] = read_text_file(path)

            elif path.suffix.lower() == ".json":
                instructions[path.name] = read_json_file(path)

    return instructions


def load_examples_from_category(category_dir):
    """
    Load all examples belonging to one category.

    Expected structure:

        category/
            example_name/
                description.md
                expected_output.md
                *.json
    """

    examples = []

    for example_dir in sorted(category_dir.iterdir()):

        if not example_dir.is_dir():
            continue

        example = {
            "name": example_dir.name,
            "description": None,
            "expected_output": None,
            "data": {}
        }

        # ----------------------------------------------------
        # Description
        # ----------------------------------------------------

        description_path = example_dir / "description.md"

        if description_path.exists():
            example["description"] = read_text_file(description_path)

        # ----------------------------------------------------
        # Expected output
        # ----------------------------------------------------

        expected_path = example_dir / "expected_output.md"

        if expected_path.exists():
            example["expected_output"] = read_text_file(expected_path)

        # ----------------------------------------------------
        # JSON files
        # ----------------------------------------------------

        for path in sorted(example_dir.glob("*.json")):
            example["data"][path.name] = read_json_file(path)

        examples.append(example)

    return examples


def load_knowledge_base(examples_dir):
    """
    Load the complete Geant4LLM knowledge base.
    """

    knowledge_base = {
        "instructions": load_instruction_files(examples_dir),
        "geometry": load_examples_from_category(
            examples_dir / "geometry"
        ),
        "source": load_examples_from_category(
            examples_dir / "source"
        ),
        "scoring": load_examples_from_category(
            examples_dir / "scoring"
        ),
        "composed": load_examples_from_category(
            examples_dir / "composed"
        )
    }

    return knowledge_base