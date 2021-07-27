# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serverOpmBxE.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #if MainWindow.objectName():
            #MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1123, 600)
        MainWindow.setStyleSheet(u"\n"
"/*VERTICAL SCROLLBAR*/\n"
"QScrollBar:vertical{\n"
"	boder: none;\n"
"	background-color: rgb(59,59,90);\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	boder-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(80,80,120);	\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"/*BIN TOP- SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical{\n"
"	border: none;\n"
"	background-color: rgb(59,59,90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;	\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	backgroung-color: rgb(255,0,127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/*BIN BOTTOM	- SCROLLBAR*/\n"
"QScrollBar::add-line:"
                        "vertical{\n"
"	border: none;\n"
"	background-color: rgb(59,59,90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;	\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"	backgroung-color: rgb(255,0,127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(56, 58, 89); ")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(210, 0, 901, 601))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background: rgb(56,56,85);\n"
"} ")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 885, 1218))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_right = QFrame(self.scrollAreaWidgetContents)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(0, 1200))
        self.frame_right.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_infor = QListWidget(self.frame_right)
        self.list_infor.setObjectName(u"list_infor")
        font = QFont()
        font.setFamily(u"Segoe UI Historic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.list_infor.setFont(font)

        self.verticalLayout_2.addWidget(self.list_infor)


        self.verticalLayout.addWidget(self.frame_right)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setGeometry(QRect(0, 0, 211, 601))
        font1 = QFont()
        font1.setPointSize(8)
        self.frame_left.setFont(font1)
        self.frame_left.setStyleSheet(u"background-color: rgb(109, 113, 173);")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_left)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 41, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.AutoText)
        self.label_2 = QLabel(self.frame_left)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 61, 51))
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.AutoText)
        self.textBrowser_port = QTextBrowser(self.frame_left)
        self.textBrowser_port.setObjectName(u"textBrowser_port")
        self.textBrowser_port.setGeometry(QRect(80, 120, 91, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.textBrowser_port.setFont(font3)
        self.textBrowser_port.setLayoutDirection(Qt.LeftToRight)
        self.textBrowser_port.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stop_btn = QPushButton(self.frame_left)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setGeometry(QRect(40, 350, 111, 31))
        self.stop_btn.setStyleSheet(u"\n"
"background-color: rgb(230, 179, 255);")
        self.textBrowser_ip = QTextBrowser(self.frame_left)
        self.textBrowser_ip.setObjectName(u"textBrowser_ip")
        self.textBrowser_ip.setGeometry(QRect(50, 40, 121, 31))
        self.textBrowser_ip.setFont(font3)
        self.textBrowser_ip.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#fbbeff;\">IP: </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#fbbeff;\">PORT: </span></p></body></html>", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

