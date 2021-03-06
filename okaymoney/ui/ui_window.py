from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class UIWindow(QMainWindow):
    """Класс окна, который автоматически подгружает UI из файла по пути,
    содержащемся в переменной класса ``ui_path``.

    Пример::

        class LoginWindow(UIWindow):
            ui_path = 'ui/login.ui'
            ...
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(self.ui_path, self)
