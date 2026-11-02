import json


# ============================================================
# PROMPT BUILDER
# ============================================================

def build_prompt(knowledge_base, user_prompt):
    """
    Build the complete prompt sent to the LLM.

    The complete knowledge base is included.
    No retrieval, filtering, inference, or interpretation
    is performed here.
    """

    sections = []

    # ========================================================
    # INSTRUCTIONS
    # ========================================================

    sections.append("=" * 70)
    sections.append("INSTRUCTIONS")
    sections.append("=" * 70)

    for filename, content in knowledge_base["instructions"].items():

        sections.append("")
        sections.append(f"--- FILE: {filename} ---")
        sections.append("")

        if isinstance(content, dict):
            content = json.dumps(
                content,
                indent=2,
                ensure_ascii=False
            )

        sections.append(content)

    # ========================================================
    # EXAMPLES
    # ========================================================

    for category in [
        "geometry",
        "source",
        "scoring",
        "composed"
    ]:

        sections.append("")
        sections.append("=" * 70)
        sections.append(f"{category.upper()} EXAMPLES")
        sections.append("=" * 70)

        for example in knowledge_base[category]:

            sections.append("")
            sections.append(
                f"--- EXAMPLE: {example['name']} ---"
            )

            # ------------------------------------------------
            # Description
            # ------------------------------------------------

            if example["description"] is not None:

                sections.append("")
                sections.append("DESCRIPTION:")
                sections.append(example["description"])

            # ------------------------------------------------
            # Expected output explanation
            # ------------------------------------------------

            if example["expected_output"] is not None:

                sections.append("")
                sections.append("EXPECTED OUTPUT EXPLANATION:")
                sections.append(example["expected_output"])

            # ------------------------------------------------
            # JSON data
            # ------------------------------------------------

            for filename, data in example["data"].items():

                sections.append("")
                sections.append(
                    f"JSON DATA ({filename}):"
                )

                sections.append(
                    json.dumps(
                        data,
                        indent=2,
                        ensure_ascii=False
                    )
                )

    # ========================================================
    # TASK
    # ========================================================

    sections.append("")
    sections.append("=" * 70)
    sections.append("TASK")
    sections.append("=" * 70)
    sections.append("")

    sections.append(
        "Translate the user's request into the IR defined by "
        "the instructions and examples above."
    )

    sections.append(
        "Return only the resulting IR as valid JSON."
    )

    sections.append(
        "Do not provide explanations."
    )

    sections.append(
        "Do not add Markdown fences."
    )

    sections.append(
        "Do not invent information that is not specified by "
        "the user or supported by the instructions and examples."
    )
    
    sections.append(
        "Preserve the exact data types required by the IR structure. "
        "All numeric values must be represented as JSON numbers, not strings."
    )

    sections.append(
        "In particular, vector components, coordinates, dimensions, "
        "radii, energies, angles, and other numerical quantities must "
        "not be enclosed in quotation marks."
    )

    # ========================================================
    # USER REQUEST
    # ========================================================

    sections.append("")
    sections.append("=" * 70)
    sections.append("USER REQUEST")
    sections.append("=" * 70)
    sections.append("")
    sections.append(user_prompt)

    # ========================================================
    # FINAL PROMPT
    # ========================================================

    return "\n".join(sections)