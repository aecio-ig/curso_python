import sys 
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import ICON_PATH
from display import Display

from main_window import MainWindow
from info import Info
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    info = Info('')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()