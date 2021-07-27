# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledcMwZgu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_tittle = QLabel(self.dropShadowFrame)
        self.label_tittle.setObjectName(u"label_tittle")
        self.label_tittle.setGeometry(QRect(60, 70, 551, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_tittle.setFont(font)
        self.label_tittle.setStyleSheet(u"color: rgb(200, 113, 189);")
        self.label_tittle.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(60, 150, 551, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(200, 113, 189);\n"
"color: rgb(140, 167, 200);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 240, 471, 31))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(140, 167, 182);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:1, y2:0.517, stop:0 rgba(200, 113, 189, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(10, 280, 641, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(200, 113, 189);\n"
"color: rgb(140, 167, 200);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.dropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 330, 291, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.label_4.setFont(font3)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(200, 113, 189);\n"
"color: rgb(140, 167, 200);")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_tittle.setText(QCoreApplication.translate("SplashScreen", u"<strong> SERVER", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"Scraping data", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"<strong> Created: </strong> Trung Hoang & Tan Phuong", None))
    # retranslateUi

