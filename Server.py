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
from datetime import datetime, date

#communicate between client - server
import socket

#create a database
import pymysql

#time update
import time
import datetime

Allow = "allow"
Not_allow = "not_allowed"
SUCCESS = "1"
FAIL = "0"
ERROR = "-1"
LOGIN = "2"
REGISTER = "3"
GOLD_SEARCHING = "4"
DISCONNECT = "5"
COMMUNICATION_TYPE = "utf-8"
BUFSIZE = 1024
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
        self.ADDR = (self.SERVER, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        print(f"Serer is listenning at:\n\tIP address: {self.SERVER}\n\tPort: {self.PORT}")
        self.server.listen()

    def accept_incoming_connections(self):
        while True:
            client, client_address = self.server.accept()
            print(f"{client_address} has connected!")

            # print(len(self.addresses))
            # if len(self.addresses) == 4:
            #     client.send('not_allowed'.encode())
            #
            #     client.close()
            #     continue
            # else:
            #     client.send('allowed'.encode())
            #
            # try:
            #     client_name = client.recv(1024).decode('utf-8')
            # except:
            #     print(f"{client_address} disconnected")
            #     client.close()
            #     continue

            self.addresses[client] = client_address
            t = Thread(target=self.handle_client, args=(client,))
            t.setDaemon(True)
            t.start()

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(BUFSIZE).decode(COMMUNICATION_TYPE)
            except ConnectionResetError:
                print(f"{self.addresses[client]} disconnected")
                del self.addresses[client]
                client.close()
                break
            except ConnectionAbortedError:
                print(f"{self.addresses[client]} disconnected unexpectedly.")
                del self.addresses[client]
                client.close()
                break

            message = message.split("/")
            print(message)
            choice = message[0]
            if choice == LOGIN:
                #login handle
                emailid = message[1]
                password = message[2]
                try:
                    con = pymysql.connect(host='localhost', user='root', password='Chelinh289', database='pythongui')
                    cur = con.cursor()
                    cur.execute('select * from register where emailid=%s and password=%s', (emailid, password))
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
                        con = pymysql.connect(host="localhost", user="root", password="Chelinh289", database="pythongui")
                        cur = con.cursor()
                        cur.execute("select * from register where emailid=%s", emailid)
                        row = cur.fetchone()
                        if row != None:
                            client.send(bytes(FAIL, COMMUNICATION_TYPE))
                        else:
                            cur.execute("insert into register values(%s,%s,%s,%s)",
                                        (username, emailid, password, confirmpassword))
                            con.commit()
                            con.close()
                            client.send(bytes(SUCCESS, COMMUNICATION_TYPE))
                    except Exception as error:
                        client.send(bytes(str(error), COMMUNICATION_TYPE))
            elif choice == GOLD_SEARCHING:
                    #gold searching handle
                    self.type = message[1]
                    self.date = message[2]

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
                        if run and run % 2 == 0:
                            self.list_price[gold_type(run)] = []
                            self.list_price[gold_type(run)].append(purchase[run - 2])
                            self.list_price[gold_type(run)].append(purchase[run - 1])

                    client.send(bytes(str(self.list_price[self.type][0]) + "/" + str(self.list_price[self.type][1]), COMMUNICATION_TYPE))
            elif choice == DISCONNECT:
                print(f"{self.addresses[client]} disconnected unexpectedly.")
                del self.addresses[client]
                client.close()
                break

if __name__ == "__main__":
    server = Server_handing()
