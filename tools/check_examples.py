"""Run the exact CPU examples displayed in the documentation, without API calls."""

import ast
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory


def main():
    root = Path(__file__).resolve().parents[1]
    examples = sorted((root / "examples").glob("*.py"))
    env = dict(os.environ, OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", MPLBACKEND="Agg")
    failures = []
    checked = 0
    for example in examples:
        ast.parse(example.read_text(encoding="utf-8"), filename=str(example))
        if example.name == "llm.py":
            print("SKIP llm.py (syntax checked; external provider required)", flush=True)
            continue
        with TemporaryDirectory(prefix="tnlearn-example-") as workdir:
            try:
                result = subprocess.run(
                    [sys.executable, str(example)],
                    cwd=workdir,
                    env=env,
                    capture_output=True,
                    text=True,
                    timeout=180,
                )
            except subprocess.TimeoutExpired:
                failures.append(example.name)
                print("FAIL {} (180-second timeout)".format(example.name), flush=True)
                continue
        checked += 1
        if result.returncode:
            failures.append(example.name)
            print("FAIL {}".format(example.name), flush=True)
            print(result.stdout)
            print(result.stderr)
        else:
            print("PASS {}".format(example.name), flush=True)
    print("{} executed, {} failed.".format(checked, len(failures)), flush=True)
    return bool(failures)


if __name__ == "__main__":
    sys.exit(main())
