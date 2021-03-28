from PySide2.QtCore import Signal, QObject
import keyboard
import logging
import time

_singleton_instance = None

class _KeyStateManager(QObject):
    hotkey_pressed = Signal()
    def __init__(self, parent=None, keys = None, hotkey_interval = 1.0, logger=None):
        super(_KeyStateManager, self).__init__(parent)
        self.logger = logging.getLogger(__name__)

        keyboard.hook(self.status_update)
        if keys is None:
            self.set_hotkeys(["ctrl", "F"])
        else:
            self.set_hotkeys(keys)
        # self.key_state = {
        #     "ctrl":"free",
        #     "F":"free"
        # }

        self.hotkey_interval = hotkey_interval

        self.previous_hotkey_time_point = 0

    # def test_hotkey_press(self):
    #     self.hotkey_pressed.emit()
    def set_hotkeys(self, keys:list):
        self.key_state = { k:"free" for k in keys }

    def status_update(self, ke : keyboard.KeyboardEvent):
        watching_keys = self.key_state.keys()
        # self.logger.debug(ke.name)
        if ke.name in watching_keys:
            self.logger.debug(f"key_state_manager: hotkey pressed: {ke.name}, {ke.event_type}")
            self.key_state[ke.name] = "pressed" if ke.event_type == "down" else "free"
            self.logger.debug(f"{self.key_state}")
            all_pressed = all([v == "pressed" for k, v in self.key_state.items()])
            if all_pressed is True:
                if time.monotonic() - self.previous_hotkey_time_point < self.hotkey_interval:
                    self.logger.info(f"in hotkey interval")
                    return
                self.hotkey_pressed.emit()
                # 一度すべてのキー状態をフリーに（UPの検知漏れ除け？）
                for k in self.key_state.keys():
                    self.key_state[k] = "free"
                self.previous_hotkey_time_point =time.monotonic()


def get_key_state_manager(parent=None):
    global _singleton_instance
    if _singleton_instance is None:
        _singleton_instance = _KeyStateManager(parent)

    return _singleton_instance
