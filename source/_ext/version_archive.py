"""Build stable and historical documentation with independent search indexes."""

from pathlib import Path
import subprocess
import sys

from sphinx.errors import ExtensionError


def build_archive(app, exception):
    if exception is not None or app.builder.name != "html":
        return
    for version in ("0.2.0", "0.1.1"):
        archive = Path(app.srcdir).parent / "archive" / version
        result = subprocess.run(
            [
                sys.executable, "-m", "sphinx", "-q", "-b", "html",
                "-E", "-a", "-n", "-W", "--keep-going",
                "-c", str(archive),
                "-d", str(Path(app.doctreedir) / ("archive-" + version)),
                str(archive / "source"),
                str(Path(app.outdir) / version),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise ExtensionError(
                "Archive {} build failed:\n{}{}".format(
                    version, result.stdout, result.stderr
                )
            )


def setup(app):
    app.connect("build-finished", build_archive)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
