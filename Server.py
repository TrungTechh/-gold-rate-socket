# this module use to design
from tkinter import *

from PySide2.QtWidgets import QApplication
from PIL import ImageTk

# multiple client
from threading import Thread, Timer
import threading

# server use this module to request party webs to reponse gold price
from bs4 import BeautifulSoup
import urllib
from urllib import request

# server use this module to update gold price
from datetime import datetime, date, timedelta

# communicate between client - server
import socket

# create a database
import mysql.connector

import time
from qtpy import QtWidgets

from random import seed, randint

# GUI
#########################################################################
import sys
import os
from typing import Counter

# IMPORTING ALL THE NECESSERY PYSIDE2 MODULES FOR OUR APPLICATION.
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QFile, Slot, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PyQt5.QtCore import QTimer
##########################################################################

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

# GLOBALS
counter = 0
class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()

        # set up GUI
        self.resize(716, 454)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self)
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
        self.label_10 = QLabel(self.dropShadowFrame)
        self.label_10.setObjectName(u"label_4")
        self.label_10.setGeometry(QRect(390, 330, 291, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.label_10.setFont(font3)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"color: rgb(200, 113, 189);\n"
                                    "color: rgb(140, 167, 200);")
        self.label_10.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        self.retrans()

        QMetaObject.connectSlotsByName(self)

        # PROCESS GUI

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(110)

        # CHANGE DESCRIPTION

        # Initial Textlabel_decsription
        self.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE "))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE "))

        ## SHOW ==> MAIN WINDOW
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    def retrans(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("Form", u"<strong> SERVER", None))
        self.label_description.setText(QCoreApplication.translate("Form", u"Scraping data", None))
        self.label_loading.setText(QCoreApplication.translate("Form", u"loading...", None))
        self.label_10.setText(
            QCoreApplication.translate("Form", u"<strong> Created: </strong> Trung Hoang & Tan Phuong", None))

    def progress(self):
        global counter

        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Ui_Server_handing()
            self.main.show()

            self.close()

        counter += 1

#GLOBAL
connected=TRUE
# server handle
class Ui_Server_handing(QWidget):

    def __init__(self):
        self.addresses = {}
        self.clients={}
        
        self.user={}
        super().__init__()

        # setupUi
        self.resize(1014, 686)
        self.setStyleSheet(u"\n"
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
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 5)
        self.frame_left = QFrame(self)
        self.frame_left.setObjectName(u"frame_left")
        font = QFont()
        font.setPointSize(8)
        self.frame_left.setFont(font)
        self.frame_left.setStyleSheet(u"background-color: rgb(109, 113, 173);")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_left)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 41, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_4 = QLabel(self.frame_left)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 61, 51))
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.text_port = QTextBrowser(self.frame_left)
        self.text_port.setObjectName(u"text_port")
        self.text_port.setGeometry(QRect(80, 120, 91, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.text_port.setFont(font2)
        self.text_port.setLayoutDirection(Qt.LeftToRight)
        self.text_port.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.text_ip = QTextBrowser(self.frame_left)
        self.text_ip.setObjectName(u"text_ip")
        self.text_ip.setGeometry(QRect(50, 40, 121, 31))
        self.text_ip.setFont(font2)
        self.text_ip.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.stop_btn_ = QPushButton(self.frame_left)
        self.stop_btn_.setObjectName(u"stop_btn_")
        self.stop_btn_.setGeometry(QRect(40, 350, 111, 31))
        self.stop_btn_.setStyleSheet(u"\n"
                                     "background-color: rgb(230, 179, 255);")
        self.stop_btn_.clicked.connect(self.stop)
        self.stop_btn_.clicked.connect(self.close)

        self.horizontalLayout.addWidget(self.frame_left)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 732, 1218))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 1200))
        self.frame_3.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.list_infor = QListWidget(self.frame_3)
        self.list_infor.setObjectName(u"list_infor")
        font3 = QFont()
        font3.setPointSize(20)
        self.list_infor.setFont(font3)
        self.list_infor.setSortingEnabled(False)

        self.verticalLayout_4.addWidget(self.list_infor)

        self.verticalLayout.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        self.setting_socket()

    
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Server", None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#fbbeff;\">IP: </span></p></body></html>",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#fbbeff;\">PORT: </span></p></body></html>",
                                                        None))      
        self.stop_btn_.setText(QCoreApplication.translate("Form", u"Stop", None))


    def setting_socket(self):
        self.PORT = 28999
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.text_ip.setText(str(self.SERVER))
        self.text_port.setText("  " + str(self.PORT))
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.SERVER, self.PORT))

        self.server.listen(10)
        th = Thread(target=self.accept_incoming_connections)
        th.setDaemon(False)
        th.start()
        #self.server.listen(10)
        
    def accept_incoming_connections(self):
        global connected
        while True:
            client, client_address = self.server.accept()
            print(f"{client_address} has connected!")
            self.addresses[client] = client_address
            t = Thread(target=self.handle_client, args=(client,))
            t.setDaemon(True)
            t.start()
            time.sleep(0.1)

    

    def handle_client(self, client):
        while True:
            try:
                message = str(client.recv(BUFSIZE).decode(COMMUNICATION_TYPE))
            except ConnectionResetError:
                print(f"{self.addresses[client]} disconnected")
                del self.addresses[client]
                client.close()
            except ConnectionAbortedError:
                print(f"{self.addresses[client]} disconnected unexpectedly.")
                del self.addresses[client]
                client.close()
            self.message = message.split("/")  # infor user
            choice = self.message[0]
            
            if choice == LOGIN:
                # login handle
                emailid = self.message[1]
                password = self.message[2]
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                                  database="gold_infor")
                    cur = con.cursor()
                    cur.execute('select * from user_table where emailid=%s and password=%s', (emailid, password))
                    row = cur.fetchone()
                    self.user[client]=emailid
                    self.list_infor.addItem(str(self.user[client]) + " with " + str(self.addresses[client]) + " connected")
                    if row == None:
                        client.send(bytes(FAIL, COMMUNICATION_TYPE))
                    else:
                        client.send(bytes(SUCCESS, COMMUNICATION_TYPE))

                except Exception as error:
                    client.send(bytes(str(error), COMMUNICATION_TYPE))
            elif choice == REGISTER:
                # regist handle
                username = self.message[1]
                password = self.message[2]
                emailid = self.message[3]
                confirmpassword = self.message[4]
                try:
                    con1 = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                                   database="gold_infor")
                    cur1 = con1.cursor()
                    cur1.execute("SELECT emailid FROM gold_infor.user_table")
                    row = cur1.fetchone()
                    # close con to creat new con

                    if row != None:
                        client.send(bytes(FAIL, COMMUNICATION_TYPE))
                    else:
                        # creat new connection
                        con = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                                      database="gold_infor")
                        cur2 = con.cursor()
                        cur2.execute(
                            "INSERT INTO gold_infor.user_table(user, emailid, password, confirmpassword) VALUES(%s,%s,%s,%s)",
                            (username, emailid, password, confirmpassword))
                        con.commit()
                        con.close()
                        client.send(bytes(SUCCESS, COMMUNICATION_TYPE))
                except Exception as error:
                    client.send(bytes(str(error), COMMUNICATION_TYPE))
            elif choice == GOLD_SEARCHING:
                # gold searching handle
                self.type = self.message[1]
                self.date = self.message[2]
                print(self.type, self.date)
                con2 = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                                database="gold_infor")
                cur2 = con2.cursor()

                cur2.execute("SELECT * FROM gold_infor.gold_table WHERE day = %s AND brand = %s", (self.date, self.type))
                result = cur2.fetchone()
                print(result)
                buy = result[2]
                sell = result[3]
                if connected==FALSE:
                    client.send(bytes(DISCONNECT, COMMUNICATION_TYPE))
                    client.close()
                else:                   
                    client.send(bytes(str(buy) + "/" + str(sell), COMMUNICATION_TYPE))
            elif choice == DISCONNECT:
                print(f"{self.addresses[client]} disconnected")
                if client in self.user.keys():
                    self.list_infor.addItem(str(self.user[client]) + " with " + str(self.addresses[client]) + " disconnected")
                    del self[client]
                del self.addresses[client]
                client.close()
                break

    def stop(self):
        global connected
        connected=FALSE

class data:
    def get_Data(self, query_insert):
        self.con = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                           database="gold_infor")
        self.cur = self.con.cursor()
        edate = date.today()  # end date
        sdate = edate - timedelta(30)  # start date

        for i in range(31):
            day = sdate + timedelta(days=i)
            self.getDataPerDay(day, query_insert)
        self.con.close()
        print("done")

    def getDataPerDay(self, day, ex):
        url = f'https://www.24h.com.vn/gia-vang-hom-nay-c425.html?d={day}'
        # grabbing the page
        cli = urllib.request.urlopen(url)
        page_html = cli.read()

        # html parsing
        page_soup = BeautifulSoup(page_html, "html.parser")

        # grab price
        prices = page_soup.find("div", {"class": "tabBody mgbt15"}).find_all("span")
        index_buy = 0
        index_sell = 2
        brands = page_soup.find("div", {"class": "tabBody mgbt15"}).find_all("h2")

        for i in brands:
            brand = i.text
            buy = prices[index_buy].text
            sell = prices[index_sell].text
            date = str(day)
            data = (buy, sell, date, brand)

            self.cur.execute(ex, data)
            self.con.commit()
            index_buy = index_buy + 4
            index_sell = index_sell + 4

    def update_data(self, query_update):
        self.con1 = mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@",
                                           database="gold_infor")
        self.cur1 = self.con1.cursor()
        edate = date.today()  # end date
        sdate = edate - timedelta(30)  # start date

        for i in range(31):
            day = sdate + timedelta(days=i)
            self.getDataPerDay_U(day, query_update)
        
        print("done")
    def getDataPerDay_U(self, day, ex):
        url = f'https://www.24h.com.vn/gia-vang-hom-nay-c425.html?d={day}'
        # grabbing the page
        cli = urllib.request.urlopen(url)
        page_html = cli.read()

        # html parsing
        page_soup = BeautifulSoup(page_html, "html.parser")

        # grab price
        prices = page_soup.find("div", {"class": "tabBody mgbt15"}).find_all("span")
        index_buy = 0
        index_sell = 2
        brands = page_soup.find("div", {"class": "tabBody mgbt15"}).find_all("h2")

        for i in brands:
            brand = i.text
            buy = prices[index_buy].text
            sell = prices[index_sell].text
            date = str(day)
            data = (buy, sell, date, brand)

            self.cur1.execute(ex, data)
            self.con1.commit()
            index_buy = index_buy + 4
            index_sell = index_sell + 4
    

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        

if __name__ == "__main__":
    # execute to insert
    query_insert = """INSERT INTO gold_infor.gold_table(buy, sell, day, brand) VALUES(%s,%s,%s,%s)"""
    # execute to update
    query_update = """ UPDATE gold_infor.gold_table
                                SET buy = %s,sell=%s
                                WHERE  day=%s AND brand =%s"""
    # Ui_Server_handing()
    get_data = data()
    new_thread = Thread(target=get_data.get_Data, args=(query_insert,))
    app = QApplication(sys.argv)
    window = SplashScreen()
    new_thread.start()
    window.show()

    update = RepeatedTimer(1800, get_data.update_data, query_update)
    sys.exit(app.exec_())
