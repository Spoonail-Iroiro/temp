import PyInstaller.__main__
from pathlib import Path


build_dir = Path(__file__).parent.parent / "Build"
distpath = build_dir / 'XSSTR'
buildpath =  build_dir / 'build'
src_dir = Path(__file__).parent

def pyinstaller_build():
    build_dir.mkdir(exist_ok=True)
    #pyinstallerでのビルド
    dist_arg = f"--distpath={distpath}"
    build_arg = f"--workpath={buildpath}"

    print(dist_arg)

    PyInstaller.__main__.run([
        "pyinstaller_main_spec.spec",
        dist_arg,
        build_arg,
        "--windowed",
        "--noconfirm",
    ])

import shutil
import os

def place_assets():
    key_dir = distpath / "key"
    key_dir.mkdir(exist_ok=True)

    assets_dir = src_dir / "assets"
    for file in assets_dir.glob("*"):
        if os.path.isfile(file):
            shutil.copy(file, distpath)
        else:
            shutil.copytree(file, distpath / file.name)

    qss_dir = src_dir / "QSS"
    shutil.copytree(qss_dir, distpath / "QSS")

    default_config_path = src_dir / "config_default.json"
    shutil.copy(default_config_path, distpath)
    shutil.copy(default_config_path, distpath / "config.json")

def clean_assets():
    for file in distpath.glob("*"):
        if os.path.isfile(file):
            os.remove(file)
        else:
            if file.name == "bin":
                continue
            shutil.rmtree(file)


pyinstaller_build()
clean_assets()
place_assets()