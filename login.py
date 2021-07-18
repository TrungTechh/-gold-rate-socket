from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import datetime
from PIL import ImageTk
import socket

#define type-communication between client and server
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

class Client_handle:
    def __init__(self, root):
        self.root = root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1920x1080+0+0")
        self.window = None
        # self.root.resizable(False, False)
        self.setting_socket()
        # self.loginform()
        self.root.protocol("WM_DELETE_WINDOW", self.closing)

    def setting_socket(self):
        self.window = "socket"

        frame_bg = Frame(self.root, bg="white")
        frame_bg.place(x=0, y=0, relheight=1, relwidth=1)

        self.img = ImageTk.PhotoImage(file=r"image/background.jpg")
        img = Label(frame_bg, image=self.img).place(x=0, y=0, relwidth=1, relheight=1)

        frame_input = Frame(frame_bg, bg="white")
        frame_input.place(relx=0.5, rely=0.5, anchor="center", width=500, height=100)

        connect_label = Label(frame_input, text="Input ip address: ", font=("Arial", 10, "bold", "italic"), fg="black", bg="white")
        connect_label.place(relx=0.005, rely=0.5, anchor="w", width=110, height=35)

        self.input_ip = Entry(frame_input, font=("Comic Sans MS", 15, "bold"), bg="lightgray")
        self.input_ip.place(relx=.45, rely=.5, anchor="center", width=220, height=35)
        self.input_ip.focus()

        self.PORT = 28999
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = Button(frame_input, text="CONNECT!", font=("Arial", 10, "bold"), cursor="hand2", command=self.setting_connection)
        connect.place(relx=0.8, rely=0.5, anchor="center", width=100, height=35)

    def setting_connection(self):
        try:
            self.client.connect((self.input_ip.get(), self.PORT))
            self.Loginform()

        except Exception as error:
            messagebox.showerror('Error', f'Error Due to : {str(error)}', parent=self.root)

    def Loginform(self):
        self.window = "login"

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, relheight=1, relwidth=1)

        self.img = ImageTk.PhotoImage(file=r"image/background.jpg")
        img = Label(Frame_login, image=self.img).place(x=0, y=0, relwidth=1, relheight=1)

        frame_input = Frame(Frame_login, bg='white')
        frame_input.place(x=600, y=200, height=450, width=350)

        main_label = Label(frame_input, text="Login Here", font=("Comic Sans MS", 32, "bold"), fg="black", bg='white')
        main_label.place(x=75, y=20)

        label1 = Label(frame_input, text="Email", font=("Comic Sans MS", 20, "bold"), fg='orangered', bg='white')
        label1.place(x=30, y=95)
        self.email_txt = Entry(frame_input, font=("Comic Sans MS", 15, "bold"), bg="lightgray")
        self.email_txt.place(x=30, y=145, width=270, height=35)

        label2 = Label(frame_input, text="Password", font=("Comic Sans MS", 20, "bold"), fg='orangered', bg='white')
        label2.place(x=30, y=195)
        self.password = Entry(frame_input, font=("Comic Sans MS", 15, "bold"), show='*', bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        #this button need to develop more-------------------------------------------------------------------------------
        btn1 = Button(frame_input, text="forgot password?", cursor='hand2', font=('calibri', 10), bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=305)
        #---------------------------------------------------------------------------------------------------------------

        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2", font=("Comic Sans MS", 15),
                      fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=90, y=340)

        btn3 = Button(frame_input, command=self.Registerform, text="Not Registered? Register", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

        self.email_txt.focus()

    def login(self):
        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                #send(
                self.client.send(bytes(LOGIN +
                                       "/" + str(self.email_txt.get()) +
                                       "/" + str(self.password.get()),
                                       COMMUNICATION_TYPE))
                #recieve
                message = str(self.client.recv(BUFSIZE).decode(COMMUNICATION_TYPE))
                print (message)
                if message == SUCCESS:
                    self.search_gold()
                elif message == FAIL:
                    messagebox.showerror('Error', 'Invalid Username And Password', parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    messagebox.showerror('Error', f'Error Due to : {str(message)}', parent=self.root)
            except ConnectionAbortedError as error:
                messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
                self.client.close()
            except ConnectionResetError as error:
                messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
                self.client.close()
                self.setting_socket()

    def Registerform(self):
        self.window = "regist"

        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=0, y=0, relheight=1, relwidth=1)
        self.img = ImageTk.PhotoImage(file=r"image/background.jpg")
        img = Label(Frame_login1, image=self.img).place(x=0, y=0, relwidth=1, relheight=1)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=500, y=200, height=450, width=630)

        main_label = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'), fg="black", bg='white')
        main_label.place(x=180, y=20)

        label1 = Label(frame_input2, text="Username", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label1.place(x=30, y=95)
        self.username = Entry(frame_input2, font=("Comin Sans MS", 15, "bold"), bg='lightgray')
        self.username.place(x=30, y=145, width=270, height=35)

        label2 = Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label2.place(x=30, y=195)
        self.password = Entry(frame_input2, font=("Comin Sans MS", 15, "bold"), show='*', bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)

        label3 = Label(frame_input2, text="Email-id", font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label3.place(x=330, y=95)
        self.emailid = Entry(frame_input2, font=("Comin Sans MS", 15, "bold"), bg='lightgray')
        self.emailid.place(x=330, y=145, width=270, height=35)

        label4 = Label(frame_input2, text="Confirm Password", font=("Goudy old style", 20, "bold"), fg='orangered',
                       bg='white')
        label4.place(x=330, y=195)
        self.confirmpassword = Entry(frame_input2, font=("Comin Sans MS", 15, "bold"), show='*', bg='lightgray')
        self.confirmpassword.place(x=330, y=245, width=270, height=35)

        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2",
                      font=("Comin Sans MS", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=220, y=340)

        btn3 = Button(frame_input2, command=self.Loginform, text="Already Registered?Login", cursor="hand2",
                      font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=230, y=390)

        self.username.focus()

    def register(self):
        if self.username.get() == "" or self.password.get() == "" or self.emailid.get() == "" or self.confirmpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.password.get() != self.confirmpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)
        else:
            try:
                self.client.send(bytes(REGISTER +
                                       "/" + str(self.username.get()) +
                                       "/" + str(self.password.get()) +
                                       "/" + str(self.emailid.get()) +
                                       "/" + str(self.confirmpassword.get()),
                                       COMMUNICATION_TYPE))
                # recieve
                message = str(self.client.recv(BUFSIZE).decode(COMMUNICATION_TYPE))
                if message == FAIL:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email", parent=self.root)
                    self.regclear()
                    self.username.focus()
                elif message == SUCCESS:
                    messagebox.showinfo("Success", "Register Succesfull", parent=self.root)
                    self.regclear()
            except ConnectionAbortedError as error:
                messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
                self.client.close()
            except ConnectionResetError as error:
                messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
                self.client.close()
                self.setting_socket()

    def search_gold(self):
        self.window = "search"

        frame_user = Frame(self.root, bg="white")
        frame_user.place(x=0, y=0, relheight=1, relwidth=1)
        self.img = ImageTk.PhotoImage(file=r"image/gold2.jpg")
        img = Label(frame_user, image=self.img).place(x=0, y=0, relwidth=1, relheight=1)

        user_input = Frame(frame_user, bg="white")
        user_input.place(relx=0.5, rely=0.5, height=500, width=900, anchor="center")

        user_mainlabel = Label(user_input, text="SEARCHING GOLD PRICE", font=("Comic Sans MS", 32, "italic", "bold"),
                               fg="red", bg="white")
        user_mainlabel.place(y=0, relwidth=1)

        user_label1 = Label(user_input, text="GOLD-TYPE", font=("calibre", 20, "bold"),
                            fg="red", bg="white")
        user_label1.place(relx=0.05, rely=0.2, anchor="w")
        option = ["DOJI HN", "DOJI SG", "MARITIME BANK", "PHU QUY SJC", "VIETINBANK GOLD", "SJC TP HCM", "SJC HA NOI",
                  "SJC DA NANG"]
        self.gold_type = Entry(user_input, font=("Comic Sans MS", 15, "bold"), bg="lightgray")
        self.gold_type.place(relx=0.05, rely=0.28, anchor="w", width=300, height=35)
        self.gold_type = ttk.Combobox(user_input, value=option)
        comboclick = Label(user_input, text=self.gold_type.get()).pack()
        self.gold_type.bind("<<ComboboxSelected>>", comboclick)
        self.gold_type.current(0)
        self.gold_type.place(relx=0.05, rely=0.28, anchor="w", width=300, height=35)

        user_label2 = Label(user_input, text="DATE", font=("calibre", 20, "bold"), fg="red", bg="white")
        user_label2.place(x=45, y=180)
        self.cal = Calendar(user_input,mindate=datetime.date(day=1, month=1, year=2018), maxdate=datetime.date.today(),
                            date_pattern="yyyy-mm-dd", selectmode="day")
        self.cal.place(x=45, y=220, height=150, width=300)

        def grad_date():
            date.config(text="Selected Date is: " + self.cal.get_date())

        get_date = Button(user_input, text="Get Date", command=grad_date).place(x=265, y=380, width=80, height=35)
        date = Label(user_input, text="")
        date.place(x=45, y=380, width=215, height=35)
        #need to fix
        self.ans = Label(user_input, borderwidth=2, relief="groove", bg="white")
        self.ans.place(relx=0.5, rely=0.2, width=400, height=300)
        #-----------------------------------------------------------------------
        searching = Button(user_input, text="SEARCHING", cursor="hand2", command=self.search)
        searching.place(relx=0.5, rely=0.95, anchor="s", width=500, height=35)

        btn2 = Button(frame_user, text="Log out", command=self.Loginform, cursor="hand2", font=("Comic Sans MS", 15),
                      fg="white", bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=1000, y=10)

    def search(self):
        date = self.cal.get_date()
        type = self.gold_type.get()
        try:
            self.client.send(bytes(GOLD_SEARCHING + "/" +
                                       self.gold_type.get() + "/" +
                                       self.cal.get_date(), COMMUNICATION_TYPE))
            ret = self.client.recv(BUFSIZE).decode(COMMUNICATION_TYPE).split("/")
            print(ret)
            out = "Date: " + date + "\nType: " + type + "\nBuying-price: " + ret[0] + "VND\nSelling-price: " + ret[1] + "VND"
            if ret:
                self.ans.config(text=out, font="Arial 20 bold", fg="black")
        except ConnectionAbortedError as error:
            messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
            self.client.close()
        except ConnectionResetError as error:
            messagebox.showerror("Error", f"Error due to:{str(error)}", parent=self.root)
            self.client.close()
            self.setting_socket()

    def closing(self):
        if self.window != "socket":
            res = messagebox.askyesno(title='Warning !', message="Do you really want to disconnect ?")
            if res:
                self.client.send(bytes(DISCONNECT, COMMUNICATION_TYPE))
                self.client.close()

        self.root.destroy()

    def regclear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.emailid.delete(0, END)
        self.confirmpassword.delete(0, END)

    def loginclear(self):
        self.email_txt.delete(0, END)
        self.password.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    ob = Client_handle(root)
    root.mainloop()
