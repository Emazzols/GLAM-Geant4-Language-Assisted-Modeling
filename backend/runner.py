import subprocess
import os
from .paths import EXECUTABLE, SIM_BUILD


def build():
    
    n_jobs = os.cpu_count() or 1

    subprocess.run(
        ["make", f"-j{n_jobs}"],
        cwd=SIM_BUILD,
        check=True
    )


def run_simulation(vis: bool):

    if vis:
        subprocess.run(
            [str(EXECUTABLE)],
            cwd=SIM_BUILD,
            check=True
        )
    else:
        subprocess.run(
            [str(EXECUTABLE), "run.mac"],
            cwd=SIM_BUILD,
            check=True
        )