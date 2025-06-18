from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QObject, Signal, Slot, QThread
from widget import Ui_myWidget
import time
import sys


class Worker(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        self.started.emit('0')
        for i in range(5):
            self.progressed.emit(str(i))
            print(i)
            time.sleep(1)
        self.finished.emit(str(5))


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork(self):
        worker = Worker()
        thread = QThread()
        
        worker.moveToThread(thread)

        thread.started.connect(worker.run)

        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        thread.start()


    def hardWork2(self):
        time.sleep(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
