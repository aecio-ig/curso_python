import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMainWindow, QStatusBar

def slot_exaple(status_bar:QStatusBar):
    status_bar.showMessage('Mensagem exibida por 1 s', timeout=1000)

def outro_slot(checked):
    print('Está marcado? ', checked)
    

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('GJGJGGJ')

menu  = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Ação 1 do primeiro menu')
primeira_acao.triggered.connect(lambda: slot_exaple(status_bar))

segunda_action = primeiro_menu.addAction('Ação 1 do primeiro menu')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)

segunda_action.hovered.connect(outro_slot)




layout = QGridLayout()
central_widget.setLayout(layout)

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 40px;')
botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 10px;')
botao3 = QPushButton('Texto do botão 2')
botao3.setStyleSheet('font-size: 10px;')


botao1.clicked.connect()


layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

status_bar = window.statusBar()
status_bar.showMessage('Sistema intregado pro crient')

window.show()

app.exec()  # O loop da aplicação