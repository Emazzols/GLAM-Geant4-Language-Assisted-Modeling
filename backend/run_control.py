from .paths import RUN_MAC, SIM_NAME_FILE

# =====================================================
# Run-level configuration
# =====================================================

def set_sim_name(name: str):
    SIM_NAME_FILE.write_text(name)


def set_num_events(n: int):
    lines = RUN_MAC.read_text().splitlines()
    out = []

    for line in lines:
        if line.strip().startswith("/run/beamOn"):
            out.append(f"/run/beamOn {n}")
        else:
            out.append(line)

    RUN_MAC.write_text("\n".join(out) + "\n")
