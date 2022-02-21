import sys
import subprocess
import shutil
import tempfile
import venv

path = tempfile.mkdtemp()
venv.create(path, with_pip = True)
subprocess.run([f"{path}/bin/pip", "install", "pyfiglet"])
subprocess.run(["python3", "-m", "figdate", *sys.argv[1:]])
shutil.rmtree(path)
