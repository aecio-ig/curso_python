# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbTest = QLabel(self.centralwidget)
        self.lbTest.setObjectName(u"lbTest")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(15)
        self.lbTest.setFont(font)
        self.lbTest.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.lbTest, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbSeuNome = QLabel(self.centralwidget)
        self.lbSeuNome.setObjectName(u"lbSeuNome")
        font1 = QFont()
        font1.setPointSize(20)
        self.lbSeuNome.setFont(font1)

        self.gridLayout_2.addWidget(self.lbSeuNome, 2, 0, 1, 1)

        self.edtNome = QLineEdit(self.centralwidget)
        self.edtNome.setObjectName(u"edtNome")

        self.gridLayout_2.addWidget(self.edtNome, 2, 1, 1, 1)

        self.btnEnviar = QPushButton(self.centralwidget)
        self.btnEnviar.setObjectName(u"btnEnviar")

        self.gridLayout_2.addWidget(self.btnEnviar, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbTest.setText(QCoreApplication.translate("MainWindow", u"TESTE TESTE! ", None))
        self.lbSeuNome.setText(QCoreApplication.translate("MainWindow", u"Seu nome:", None))
        self.edtNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.btnEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

