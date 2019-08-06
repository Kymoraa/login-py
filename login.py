from tkinter import *
import sqlite3

# Setting up the main frame
root = Tk()
root.title("Python: Simple Login Application")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# Variables
USERNAME = StringVar()
PASSWORD = StringVar()

# Frames
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

# Labels
label_title = Label(Top, text="Login Application", font=('arial', 15))
label_title.pack(fill=X)
label_username = Label(Form, text="Username", font=('arial', 14), bd=15)
label_username.grid(row=0, sticky="e")
label_password = Label(Form, text="Password", font=('arial', 14), bd=15)
label_password.grid(row=1, sticky="e")
label_text = Label(Form)
label_text.grid(row=2, columnspan=2)

# Entry widgets
username = Entry(Form, textvariable=USERNAME, font=14)
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=14)
password.grid(row=1, column=1)


# Database connection
def Database():
    global conn, cursor
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'users' (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username "
                   "TEXT, password TEXT)")
    cursor.execute("SELECT * FROM 'users' WHERE 'username' = 'admin' AND 'password' = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO 'users' (username, password) VALUES('admin', 'admin')")
        conn.commit()


# The main function
def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        label_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM 'users' WHERE 'username' = ? AND 'password' = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            label_text.config(text="")
        else:
            label_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Home Page")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    label_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    button_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)


# Button widgets
button_login = Button(Form, text="Login", width=45, command=Login)
button_login.grid(pady=25, row=3, columnspan=2)
button_login.bind('<Return>', Login)


def Back():
    Home.destroy()
    root.deiconify()


# Initialization
if __name__ == '__main__':
    root.mainloop()