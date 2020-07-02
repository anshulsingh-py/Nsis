import os
import shutil
import subprocess
def Path(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name)
path=Path('tex')
if path is None:
    subprocess.call("miktex-x64.exe")