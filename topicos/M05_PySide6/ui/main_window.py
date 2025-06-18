from window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnEnviar.clicked.connect(self.changeLabelResult)
    
    def changeLabelResult(self):
        text = self.edtNome.text()
        self.lbTest.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
