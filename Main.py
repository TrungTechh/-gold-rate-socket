#multiple client
from os import spawnl
from threading import Thread

#server use this module to request party webs to reponse gold price
from bs4 import BeautifulSoup
import urllib
from urllib import request

#server use this module to update gold price
from datetime import datetime, date,timedelta

#communicate between client - server
import socket

#create a database
import mysql.connector

import time

Allow = "allow"
Not_allow = "not_allowed"

LOGIN = "2"
REGISTER = "3"
GOLD_SEARCHING = "4"
DISCONNECT = "5"
COMMUNICATION_TYPE = "utf-8"
BUFSIZE = 1024

SUCCESS = "1"
FAIL = "0"
ERROR = "-1"
SECOND = 100
MINUTE = 60 * SECOND

import sys
from typing import Counter

#IMPORTING ALL THE NECESSERY PYSIDE2 MODULES FOR OUR APPLICATION.
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


from ui_splash_screen import Ui_SplashScreen

from ui_server import Ui_MainWindow


## ==> GLOBALS
counter = 0
'''
class Server_handing(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Server_handing()
        self.ui.get_Data()
'''
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.data=Ui_Server_handing()
        #self.data.setting_socket()
        #server=self.data.SERVER
        #port=self.data.PORT
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.textBrowser_ip.setText(str(server))
        #self.ui.textBrowser_port.setText("  "+str(port))
        
        #while True:
            #self.data.accept_incoming_connections()
            #self.ui.list_infor.addItem(self.data.message[1])
        
        self.ui.list_infor.addItem("Trung")

        # MAIN WINDOW LABEL
        #QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        #QtCore.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_SplashScreen()
        self.ui.setupUi(self)

         ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Textlabel_decsription
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.t = MainWindow()
            self.t.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__== "__main__":
    app = QApplication(sys.argv)
    window=SplashScreen()
    #t=Thread(target=Server_handing)
    #t.start()
    window.show()
    sys.exit(app.exec_())
    
    