from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from variables import MEDIUM_FONT_SIZE
from utils import isNUmOrDot, isEmpty, isValidNumber
from main_window import MainWindow
from typing import TYPE_CHECKING

if TYPE_CHECKING:
        from display import Display
        from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display, info, window:MainWindow,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._GridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._MakeGrid()
        self.info = info
        self.window = window
        self._equation = ''
        self._left = None
        self._rigth = None
        self._op = None
        self.equation = ''

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _MakeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i , row in enumerate(self._GridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                self.addWidget(button, i, j)

                if not isNUmOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'especialButton') 
                    self._configSpecialButton(button)   

                else:
                    slot = self._makeSlot(
                        self._insertToDisplay, 
                        buttonText
                    )  
                    button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'D':
            self._connectButtonClicked(button, self._clear)

        if text == 'C':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._configLeftOp, button.text())
            )

        if text == '=':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._eq)
            )

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newValueDisplay = self.display.text() + text

        if not isValidNumber(newValueDisplay):
            return
        
        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._op = None
        self._left = None
        self._rigth = None
        self.display.clear()
        self.info.setText('')

    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            return
        
        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op}'

    @Slot()
    def _eq(self):
        displayText = self.display.text()
        result = 'error'

        if not isValidNumber(displayText):
            return
        
        self._rigth = float(displayText)
        self.equation = f'{self._left} {self._op} {self._rigth}'

        try:
            equacao = self.equation.replace('^', '**')
            result = eval(equacao)
        except ZeroDivisionError:
            self._showError('Divizão por zero.')
        except OverflowError:
            self._showError('Número muito grande.')
        
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        self._left = result
        self._rigth = None

        if result == 'error':
            self._left = None

    def _showError(self, texto):
        msgBox = self.window.makeMessageBox()
        msgBox.setText(texto)
        msgBox.setIcon(msgBox.Icon.Critical)

        msgBox.setInformativeText('Aqui temos o dialogo de informativo referente ao suposto erro')

        msgBox.setStandardButtons(
            msgBox.StandardButton.NoToAll|msgBox.StandardButton.Ok
        )

        msgBox.button(msgBox.StandardButton.NoToAll).setText('Não para todes!')

        result = msgBox.exec()

        ## é retornado o proprio obtão

        if result == msgBox.StandardButton.NoToAll: 
            print('clicou em no to all')
        
        if result  == msgBox.StandardButton.Ok:
            print('clicou em ok')