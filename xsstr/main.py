from PySide2.QtWidgets import QApplication
from . import __version__
# from .forms.main_form import MainForm
from .forms.main_form_window import MainFormWindow
from .forms.capture_form import CaptureForm
from pathlib import Path
import logging
import sys, ctypes, shutil
from .config import Config
from .util import *

def prepare_logging():
    if getattr(sys, 'frozen', False):
        log_level = logging.WARNING
    else:
        log_level = logging.DEBUG

    basic_format = "%(levelname)s:%(threadName)s:%(name)s:%(message)s"
    logging.basicConfig(level=log_level, format=basic_format)
    root_logger = logging.getLogger()

    fh = logging.FileHandler(error_log_path, "w", encoding="utf-8")
    fh.setLevel(logging.WARNING)
    fh.setFormatter(logging.Formatter(basic_format))
    root_logger.addHandler(fh)

def main():
    prepare_logging()

    logger = logging.getLogger(__name__)

    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        logger.warning("High DPI setting failed")

    try:
        if not config_path.exists():
            shutil.copy(default_config_path, config_path)
        Config.load_config(str(config_path))

        app = QApplication(sys.argv)

        qss_path = application_dir / "QSS"/ "MyDark2_borderless.qss"
        style = qss_path.read_text(encoding="utf-8")
        app.setStyleSheet(style)

        form = MainFormWindow()
        # from .forms.main_form import MainForm
        # form = MainForm()

        # form.setStyleSheet(orig_style)
        # form = CaptureForm()
        # form.setPicPath(str(pic_path))
        # print(form.style().)
        # form.setWindowTitle(f"XSSTR v{__version__}")

        form.show()

        code = app.exec_()

        #configをファイルに記録（もし記憶するような項目がある場合、ここまででConfig.configを変更する）
        Config.save_config(config_path)

        sys.exit(code)

    except Exception as ex:
        import traceback
        message = traceback.format_exc()
        logger.error(message)
        raise

if __name__ == "__main__":
    main()

