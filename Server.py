#this module use to design
from codecs import ignore_errors
from tkinter import *

from PySide2.QtWidgets import QApplication
from ui_splash_screen import Ui_SplashScreen
from PIL import ImageTk

#multiple client
from threading import Thread
import threading

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
from qtpy import QtWidgets
from qt_thread_updater import get_updater

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
#GUI
#########################################################################
import sys
from typing import Counter

#IMPORTING ALL THE NECESSERY PYSIDE2 MODULES FOR OUR APPLICATION.
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen

from ui_server import Ui_MainWindow
from PyQt5.QtCore import QTimer
##########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

#server handle
class Ui_Server_handing(QMainWindow):
    def __init__(self):
        self.addresses = {}
        self.clients = {}

        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        th = threading.Thread(target=self.show())

        self.m=Ui_MainWindow()
        self.m.setupUi(self)
        th2 = threading.Thread(target=self.accept_incoming_connections)
        th3 = threading.Thread(target=self.setting_socket)
        th.start()

        th3.start()


        th2.start()
        

        
    def setting_socket(self):
        self.PORT = 28999
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        self.m.textBrowser_ip.setText(str(self.SERVER))
        self.m.textBrowser_port.setText( "  "+str(self.PORT))
        #get_updater().call_latest(self.ui.textBrowser_port.setText, "  "+str(self.PORT))

        #print(f"Serer is listenning at:\n\tIP address: {self.SERVER}\n\tPort: {self.PORT}")
        self.server.listen()
    
   

    def accept_incoming_connections(self):
        while True:
            client, client_address = self.server.accept()
            print(f"{self.client_address} has connected!")
            # client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
            self.addresses[client] = client_address
            self.m.list_infor.addItem("trung")
            t = Thread(target=self.handle_client, args=(client,))
            t.setDaemon(True)
            t.start()
            time.sleep(0.5)

    
    def get_Data(self):
        self.con =  mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@", database="gold_infor")
        self.cur = self.con.cursor()

        #execute to insert
        self.query_insert="""INSERT INTO gold_infor.gold_table(buy, sell, day, brand) VALUES(%s,%s,%s,%s)"""
        #execute to update        
        query_update = """ UPDATE gold_infor.gold_table
                                SET buy = %s,sell=%s
                                WHERE  day=%s AND brand =%s"""


                

       
        edate = date.today()# end date
        sdate=edate-timedelta(30)  #start date
                    
        for i in range(31):
            day = sdate + timedelta(days=i)
            self.getDataPerDay(day)
        print("done")

    def getDataPerDay(self,day):
        url=f'https://www.24h.com.vn/gia-vang-hom-nay-c425.html?d={day}'
                    #grabbing the page
        client=urllib.request.urlopen(url)
        page_html=client.read()

                    #html parsing
        page_soup=BeautifulSoup(page_html,"html.parser")

         #grab price
        prices=page_soup.find("div",{"class":"tabBody mgbt15"}).find_all("span")
        index_buy=0
        index_sell=2
        brands= page_soup.find("div",{"class":"tabBody mgbt15"}).find_all("h2")

        for i in brands:
            brand=i.text
            buy=prices[index_buy].text
            sell=prices[index_sell].text
            date=str(day)
            data=(buy,sell,date,brand)
                        
            self.cur.execute(self.query_insert,data)
            self.con.commit()       
            index_buy=index_buy+4
            index_sell=index_sell+4

    
    
    def handle_client(self, client):
        
        while True:
            try:
                message = str(client.recv(BUFSIZE).decode(COMMUNICATION_TYPE))
            except ConnectionResetError:
                print(f"{self.addresses[client]} disconnected")
                del self.addresses[client]
                client.close()
                self.dis=0
            except ConnectionAbortedError:
                print(f"{self.addresses[client]} disconnected unexpectedly.")
                del self.addresses[client]
                client.close()
                self.dis=0
            self.message = message.split("/")#infor user 
            #print(self.message[1])

            get_updater().call_latest(self.m.list_infor.addItem, str(self.message[1]))
##################################################################################################
            choice = self.message[0]
            if choice == LOGIN:
                #login handle
                emailid = self.message[1]
                password = self.message[2]
                try:
                    con = mysql.connector.connect(host='localhost', user='root', password='Tuilawibu123@', database='gold_infor')
                    cur = con.cursor()
                    cur.execute('select * from user_table where emailid=%s and password=%s', (emailid, password))
                    row = cur.fetchone()
                    if row == None:
                        client.send(bytes(FAIL, COMMUNICATION_TYPE))
                    else:
                        client.send(bytes(SUCCESS, COMMUNICATION_TYPE))
                except Exception as error:
                    client.send(bytes(str(error), COMMUNICATION_TYPE))
            elif choice == REGISTER:
                #regist handle
                username = message[1]
                password = message[2]
                emailid = message[3]
                confirmpassword = message[4]
                try:
                    con =  mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@", database="gold_infor")
                    cur = con.cursor()
                    cur.execute("SELECT emailid FROM gold_infor.user_table")
                    row = cur.fetchone()
                    #close con to creat new con
                    con.close()
                    if row == None:
                        client.send(bytes(FAIL, COMMUNICATION_TYPE))
                    else:
                        #creat new connection
                        con =  mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@", database="gold_infor")
                        cur2=con.cursor()
                        cur2.execute("INSERT INTO gold_infor.user_table(user, emailid, password, confirmpassword) VALUES(%s,%s,%s,%s)",
                        (username,emailid,password,confirmpassword))
                        con.commit()
                        con.close()
                        client.send(bytes(SUCCESS, COMMUNICATION_TYPE))
                except Exception as error:
                    client.send(bytes(str(error), COMMUNICATION_TYPE))

            elif choice == GOLD_SEARCHING:
                #gold searching handle
                self.type = message[1]
                self.date = message[2]
                
                con2 =  mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@", database="gold_infor")
                cur2 = con2.cursor()
                
                cur2.execute("SELECT * FROM gold_infor.gold_table WHERE day = %s AND brand = %s",(self.date,self.type))
                result = cur2.fetchone()
                self.buy = result[2]
                self.sell = result[3]
                print(self.buy,self.sell)
                
                client.send(bytes(str(self.buy) + "/" + str(self.sell),COMMUNICATION_TYPE))

if __name__=="__main__":
    #Ui_Server_handing()
    app = QApplication(sys.argv)
    window=Ui_Server_handing()
    
    sys.exit(app.exec_())

