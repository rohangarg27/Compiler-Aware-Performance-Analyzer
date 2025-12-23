import subprocess
import os
from pathlib import Path

FLAGS = ["-O0", "-O1", "-O2", "-O3"]

def compile_source(src):
    src = Path(src)
    name = src.stem

    os.makedirs("bin", exist_ok=True)
    os.makedirs("results/compiler", exist_ok=True)

    binaries = []

    for flag in FLAGS:
        out = f"bin/{name}{flag.replace('-', '')}"
        report = f"results/compiler/{name}_{flag.replace('-', '')}.txt"

        cmd = [
            "clang++",
            str(src),
            flag,
            "-march=native",
            "-ftime-report",
            "-Rpass=.",
            "-o", out
        ]

        print("Compiling:", " ".join(cmd))
        with open(report, "w") as f:
            subprocess.run(cmd, stderr=f, stdout=subprocess.DEVNULL, check=True)

        binaries.append((flag, out))

    return binaries


