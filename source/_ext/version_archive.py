"""Build the historical documentation with its own navigation and search."""

from pathlib import Path
import subprocess
import sys

from sphinx.errors import ExtensionError


def build_archive(app, exception):
    if exception is not None or app.builder.name != "html":
        return
    archive = Path(app.srcdir).parent / "archive" / "0.1.1"
    result = subprocess.run(
        [
            sys.executable, "-m", "sphinx", "-q", "-b", "html",
            "-a", "-W", "--keep-going",
            "-c", str(archive),
            "-d", str(Path(app.doctreedir) / "archive-0.1.1"),
            str(archive / "source"),
            str(Path(app.outdir) / "0.1.1"),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise ExtensionError("Archive build failed:\n" + result.stdout + result.stderr)


def setup(app):
    app.connect("build-finished", build_archive)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
