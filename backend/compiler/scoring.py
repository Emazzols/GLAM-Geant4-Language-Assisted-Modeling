def compile_scoring(scoring):
    lines = []
    lines.append("// --- Scoring generated from IR ---")

    for name in scoring:
        lines.append(f'run->RegisterObservable(LV("{name}"));')

    return "\n".join(lines)
