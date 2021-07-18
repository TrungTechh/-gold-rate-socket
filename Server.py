#this module use to design
from tkinter import *
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

LOGIN = "1"
REGISTER = "2"
GOLD_SEARCHING = "3"
COMMUNICATION_TYPE = "utf-8"
BUFSIZ = 1024
SUCCESS = "1"
FAIL = "0"
SECOND = 100
MINUTE = 60 * SECOND

class Server_handing:
    def __init__(self):
        self.addresses = {}
        self.clients = {}
        self.list_price = {}
        self.setting_socket()
        self.accept_incoming_connections()

    def setting_socket(self):
        self.PORT = 28999
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        print(f"Serer is listenning at:\n\tIP address: {self.SERVER}\n\tPort: {self.PORT}")
        self.server.listen(10)

    def accept_incoming_connections(self):
        while True:
            client, client_address = self.server.accept()
            print(f"{client_address} has connected!")
            # client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
            self.addresses[client] = client_address
            Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            message = str(client.recv(BUFSIZ).decode(COMMUNICATION_TYPE)).split("/")
            choice = message[0]
            if choice == LOGIN:
                #login handle
                emailid = message[1]
                password = message[2]
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
                print(username+'\n'+password+'\n'+emailid+'\n'+confirmpassword)
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
            else:
                #gold searching handle
                self.type = message[1]
                self.date = message[2]

                print(self.type)
                print(self.date)
                #data base connect
                con =  mysql.connector.connect(host="localhost", user="root", password="Tuilawibu123@", database="gold_infor")
                cur = con.cursor()

                #execute to insert
                query_insert="""INSERT INTO gold_infor.gold_table(buy, sell, day, brand) VALUES(%s,%s,%s,%s)"""
                #execute to update
                query_update = """ UPDATE gold_infor.gold_table
                                SET buy = %s,sell=%s
                                WHERE  day=%s AND brand =%s"""

                def getDataPerDay(day,ex):
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
                        day=str(day)
                        data=(buy,sell,day,brand)
                        
                        cur.execute(ex,data)
                        con.commit()       
                        index_buy=index_buy+4
                        index_sell=index_sell+4

                def get_Data(ex):
                    sdate = date(2021, 7, 14)   # start dat
                    edate = date.today()   # end date
                    
                    for i in range(31):
                        day = sdate + timedelta(days=i)
                        getDataPerDay(day,ex)

                def getData():
                    get_Data(query_insert)

                def updateData():
                    while True:
                        get_Data(query_update)
                        print("Data will update after: ")
                        countdown()
                        print('Updated')
                        
                #count down 30 minutes
                def countdown():
                    t=30*60
                    while t:
                        mins, secs = divmod(t, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        print(timer, end="\r")
                        time.sleep(1)
                        t -= 1                    
                    

                cursor1 = con.cursor()
                cursor1.execute("SELECT * FROM gold_infor.gold_table WHERE day = %s AND brand = %s",(self.date,self.type))
                result = cursor1.fetchone()
                buy = result[2]
                sell = result[3]
                print(buy,sell)
                client.send(bytes(str(buy) + "/" + str(sell),COMMUNICATION_TYPE))
                
                
                '''
                print(type(self.type))
                print(type(self.date))
                page = urllib.request.urlopen(f"https://www.24h.com.vn/gia-vang-hom-nay-c425.html?d={self.date}").read()
                html = BeautifulSoup(page, "html.parser")
                price = html.find_all(class_="fixW")

                self.list_price.clear()
                purchase = []
                run = 0

                def gold_type(run):
                    if run / 2 == 1:
                        return "DOJI HN"
                    elif run / 2 == 2:
                        return "DOJI SG"
                    elif run / 2 == 3:
                        return "MARITIME BANK"
                    elif run / 2 == 4:
                        return "PHU QUY SJC"
                    elif run / 2 == 5:
                        return "VIETINBANK GOLD"
                    elif run / 2 == 6:
                        return "SJC TP HCM"
                    elif run / 2 == 7:
                        return "SJC HA NOI"
                    elif run / 2 == 8:
                        return "SJC DA NANG"

                for p in price:
                    run = run + 1
                    p = str(p)[19:29]
                    purchase.append(p)
                    # print(p[19:29])
                    print(p)
                    if run and run % 2 == 0:
                        self.list_price[gold_type(run)] = []
                        self.list_price[gold_type(run)].append(purchase[run - 2])
                        self.list_price[gold_type(run)].append(purchase[run - 1])
                print(str(self.list_price[self.type][0]) + "/" + str(self.list_price[self.type][1]))
                client.send(bytes(str(self.list_price[self.type][0]) + "/" + str(self.list_price[self.type][1]),COMMUNICATION_TYPE    ))
                '''


if __name__ == "__main__":
    server = Server_handing()
