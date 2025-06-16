import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGridLayout

app = QApplication(sys.argv)


botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 10px;')


botao3 = QPushButton('Texto do botão 2')
botao3.setStyleSheet('font-size: 10px;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 2)

layout.addWidget(botao3, 1, 2, 1, 3)


central_widget.show()

app.exec()  # O loop da aplicação