from tkinter import *
from tkinter import GROOVE  # Import GROOVE from Tkinter
from Exscript.protocols import SSH2
from Exscript import Host, Account
import re
import csv

window = Tk()
window.geometry('500x500+400+150')
window.title('Test')

# Load the image
photo = PhotoImage(file='logo.png')

def f1():
    try:
        with open('credentials and Router IP.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                account1 = Account('{0}'.format(line[0]), '{0}'.format(line[1]))
                break

        conn = SSH2()
        conn.connect('aterm.tedata.net', '9090')
        conn.set_prompt([re.compile(r"[\$]")])
        conn.login(account1)
        conn.set_prompt([re.compile(r"[:]")])
        conn.execute('telnet {0}'.format(line[4]))
        print(conn.response)
        conn.execute('{0}'.format(line[2]))
        print(conn.response)
        conn.set_prompt([re.compile(r"[#]")])
        conn.execute('{0}'.format(line[3]))
        print(conn.response)
        conn.set_prompt([re.compile(r"[#]")])

        csv_file = open('input.csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        count_line = 0

        for row in csv_reader:
            count_line += 1
            print("Now working on # {0}:".format(count_line))
            print(row)
            conn.execute('conf t')
            print("Now enter Config level !!")
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('no interface {0}'.format(row[0]))
            print("NO interface {}".format(row[0]))
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('l2vpn xconnect group {0}'.format(row[1]))
            print("l2vpn xconnect group {0}".format(row[1]))
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('no p2p {0}'.format(row[2]))
            print(conn.response)
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('show commit changes diff')
            print(conn.response)
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('commit')
            print(conn.response)
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('exit')
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('exit')
            conn.set_prompt([re.compile(r"[#]")])
            conn.execute('exit')

        value = input("Please press enter to exit prompt # ....... ")
    except Exception as e:  # Catch specific exceptions
        print(f"Error: {e}")
        value = input("Press any key to exit prompt # ....... ")

# Use Label to display the image
mlabel4 = Label(window, image=photo)
mlabel4.place(x=20, y=25)

Button(text='Submit', relief=GROOVE, fg="red", cursor="hand2", font=("arial", 16, "bold"), command=f1).place(x=210, y=400)

Label(text="Aterm Username:", font=("arial", 12, "bold")).place(x=50, y=150)
Label(text="Aterm Password:", font=("arial", 12, "bold")).place(x=50, y=200)
Label(text="Login Username:", font=("arial", 12, "bold")).place(x=50, y=250)
Label(text="Aterm Password:", font=("arial", 12, "bold")).place(x=50, y=300)

window.mainloop()

