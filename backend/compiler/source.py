from backend.ir.units import energy, vector3, length

def compile_source(source):
    lines = []
    lines.append("// --- Source generated from IR ---")

    lines.append(f'gen->SetParticle("{source["particle"]}");')
    lines.append(f'gen->SetMonoEnergy({energy(source["energy"])});')

    pos = vector3(source["position"])

    if source["type"] == "point":
        lines.append(f'gen->SetPointSource({pos});')

    elif source["type"] == "disk":
        lines.append(
            f'gen->SetDiskSource({length(source["radius"])}, {pos});'
        )

    elif source["type"] == "sphere":
        lines.append(
            f'gen->SetSphereSource({length(source["radius"])}, {pos});'
        )

    if source.get("isotropic", False):
        lines.append("gen->SetIsotropic();")
    else:
        d = source["direction"]
        lines.append(
            f'gen->SetDirectional(G4ThreeVector({d[0]}, {d[1]}, {d[2]}).unit());'
        )

    return "\n".join(lines)
