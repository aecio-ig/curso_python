from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal

from utils import isEmpty, isNUmOrDot

from variables import BIG_FONT_SIZE, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str) ## Aqui na criação do signal tem que passar um algumento seeeee necessario de argumento
    operatorPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelet = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk]
        


        if isEnter:
            print('Pressionado enter')
            self.eqPressed.emit()
            return event.ignore()

        if isDelet:
            print('Pressionado del')
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            print('Pressionado clear')
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            print('Pressionado operator')
            self.clearPressed.emit()
            return event.ignore()
        
        
        if isEmpty(text):
            return event.ignore()
        
        if isNUmOrDot(text):
            self.inputPressed().emit(text)
            return event.ignore()


        
        print('Texto', text)