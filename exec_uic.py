from pathlib import Path
import subprocess

forms_dir = Path(__file__).parent / "xsstr" / "forms"

ui_paths = list(forms_dir.glob("*.ui"))

for path in ui_paths:
    cmd = f'pyside2-uic "{path}" -o "{path.with_name(path.stem + "_ui").with_suffix(".py")}" '
    print(cmd)
    subprocess.run(cmd)