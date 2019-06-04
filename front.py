from tkinter import *
import tkinter.messagebox
import app1
import os

v = """ 



JAYz Notepad>>>>>>>>>
Contains:
1.Save as tab>> User is required to fill this tab in order to save the file with the name in this tab.
2.Open tab>> User is required to fill this tab in order to open a exixting file or to create a new one.
3.DICTIONARY tab>> user id required to fill this tab in order to search for the meaning of any word.
4.Save button>> Click it if you want to save the file.The save as tab should be filled before clicking this.
5.Open button>> Click it if you want to open a new or existing file.The open tab should be filled before clicking it.
6.File are generated in the same Folder as the application.
"""


def about():
    Text_main.insert(END, v)


def translate():
    Text_dict.delete("1.40", END)
    c = app1.translate(e3.get())
    if type(c) == str:
        Text_dict.insert(END, c)
    e3.delete("0", END)


def save():
    q = e1.get() + ".txt"
    w = Text_main.get("1.0", END)
    if e1.get() == "":

        tkinter.messagebox.showinfo("NAME", "Please enter a name for the file")
    else:
        if e1.get() == e2.get():
            os.remove(q)
            f = open(q, "w")
            f.write(w)
            f.close()
            e1.delete("0", END)
            e2.delete("0", END)
            Text_main.delete("1.0", END)
            tkinter.messagebox.showinfo("SAVED", "File is saved")
        elif e2.get() == "":
            try:
                f = open(q, 'r')
                f.close()
                j = tkinter.messagebox.askquestion("REPLACE", "Want to replace the file?")
                if j == "yes":
                    os.remove(q)
                    f = open(q, "w")
                    f.write(w)
                    f.close()
                    tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                    e1.delete("0", END)
                    Text_main.delete("1.0", END)
                    e2.delete("0", END)
                else:
                    tkinter.messagebox.showinfo("Choose", "Please enter a different name")

            except FileNotFoundError:
                f = open(q, "w")
                f.write(w)
                f.close()
                tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                e1.delete("0", END)
                e2.delete("0", END)
                Text_main.delete("1.0", END)

        else:
            k = tkinter.messagebox.askquestion("CHANGE", "Want to change the name of file?")
            if k == "yes":
                try:
                    f = open(e1.get(), "r")
                    f.close()
                    tkinter.messagebox.showinfo("WARNING", "File with name already there!!!")

                except FileNotFoundError:
                    x = e1.get()+".txt"
                    os.remove(e2.get()+".txt")
                    f = open(x, "w")
                    f.write(w)
                    f.close()
                    tkinter.messagebox.showinfo("SAVED", "File is saved")
                    e1.delete('0', END)
                    e2.delete("0", END)
                    Text_main.delete("1.0", END)
            else:
                tkinter.messagebox.showinfo("WARNING", "Enter different name..")


def open_new():
    if e2.get() == "":
        tkinter.messagebox.showinfo("WARNING", "ENTER THE NAME FOR NEW FILE IN OPEN TAB!!!! ")
    else:
        if Text_main.get("1.0", END) == "\n":
            d = e2.get() + ".txt"
            try:
                f = open(d, "r")
                f.close()
                tkinter.messagebox.showinfo("FILE EXIST", "File with same name is already there!!")
            except FileNotFoundError:
                f = open(d, "w")
                f.close()
                tkinter.messagebox.showinfo("CREATED", 'FILE IS CREATED!')
                e1.delete("0", END)
                e1.insert(END, e2.get())
        else:
            s = tkinter.messagebox.askquestion("SAVE", "Do you want to save the file on board")
            if s == "yes":
                q = e1.get() + ".txt"
                w = Text_main.get("1.0", END)
                if e1.get() == "":
                    tkinter.messagebox.showinfo("WARNING", "Enter the name of file in save as..")
                else:
                    if e1.get() == e2.get():
                        os.remove(q)
                        f = open(q, "w")
                        f.write(w)
                        f.close()
                        tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                        tkinter.messagebox.showinfo("OPENED", "New file is opened")
                        e1.delete("0", END)
                        e1.insert(END, e2.get())
                    else:
                        try:
                            f = open(q, 'r')
                            f.close()
                            s = tkinter.messagebox.askquestion("REPLACE", "File with same name exist.Want to replace?")
                            if s == "yes":
                                os.remove(q)
                                f = open(q, "w")
                                f.write(w)
                                f.close()
                                tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                                e1.delete("0", END)
                                e1.insert(END, e2.get())
                            else:
                                tkinter.messagebox.showinfo("Choose", "Please enter a different name")

                        except FileNotFoundError:
                            f = open(q, "w")
                            f.write(w)
                            f.close()
                            tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                            e1.delete("0", END)
                            e1.insert(END, e2.get())

    Text_main.delete("1.0", END)


def open_old():
    if e2.get() == "":
        tkinter.messagebox.showinfo("WARNING", "ENTER THE NAME FOR FILE TO OPEN!!!! ")
    else:
        if Text_main.get("1.0", END) == "\n":
            d = e2.get() + ".txt"
            try:
                f = open(d, "r")
                d = f.read()
                f.close()
                Text_main.insert(END, d)
                tkinter.messagebox.showinfo("FILE EXIST", "File opened")
                e1.delete("0", END)
                e1.insert(END, e2.get())

            except FileNotFoundError:
                tkinter.messagebox.showinfo("WARNING", 'NO FILE WITH THIS NAME!')
                e2.delete("0", END)

        else:
            s = tkinter.messagebox.askquestion("SAVE", "Do you want to save the file on board")
            if s == "yes":
                q = e1.get() + ".txt"
                w = Text_main.get("1.0", END)
                if e1.get() == "":
                    tkinter.messagebox.showinfo("WARNING", "Enter the name of file in save as..")
                else:
                    if e1.get() == e2.get():
                        f = open(q, "w")
                        f.write(w)
                        f.close()
                        tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                        tkinter.messagebox.showinfo("OPENED", " file is opened")
                        e1.delete("0", END)
                        e1.insert(END, e2.get())
                    else:
                        try:
                            f = open(q, 'r')
                            f.close()
                            s = tkinter.messagebox.askquestion("REPLACE", "File with same name exist.Want to replace?")
                            if s == "yes":
                                f = open(q, "w")
                                f.write(w)
                                f.close()
                                tkinter.messagebox.showinfo("SAVED", "Your file is saved")
                                tkinter.messagebox.showinfo("Open", "File is opened")
                                e1.delete("0", END)
                                e1.insert(END, e2.get())
                            else:
                                tkinter.messagebox.showinfo("Choose", "Please enter a different name")

                        except FileNotFoundError:
                            tkinter.messagebox.showinfo("WARNING", "File doesn't exists")


window = Tk()
window.configure(background="black")
window.title("JAYz Notepad")


men = Menu(window)
men.config(background='black')
window.config(menu=men)

first = Menu(men)
men.add_cascade(label="File", menu=first)
first.add_command(label="New", command=open_new)
first.add_command(label="Open", command=open_old)
first.add_command(label="Save", command=save)
first.add_command(label="Exit", command=window.destroy)


third = Menu(men)
men.add_cascade(label="about", menu=third)
third.add_command(label="View", command=about)


l = Label(window, text="Save as..", bg="red", fg="black", font=56, padx=14, pady=14)
l.grid(row=0, column=15)
b2 = Button(window, text="Save", bg="light blue", border=8, height=2, width=8, command=save)
b2.grid(row=0, column=16)

l2 = Label(window, text="Open file..", bg="red", fg="black", font=56, padx=14, pady=14)
l2.grid(row=2, column=15)

b3 = Button(window, text="Open", bg="light blue", border=8, height=2, width=8, command=open_old)
b3.grid(row=2, column=16)

t2 = StringVar()
e2 = Entry(window, textvariable=t2, font=8)
e2.grid(row=3, column=15)

t3 = StringVar()
e3 = Entry(window, textvariable=t3, font=8)
e3.grid(row=6, column=15)

l2 = Label(window, text="font size", bg="red", fg="black", font=56, padx=14, pady=14)
l2.grid(row=22, column=15)

b1 = Button(window, text="SEARCH...", bg="light blue", border=8, height=2, width=10, command=translate)
b1.grid(row=7, column=15)


t1 = StringVar()
e1 = Entry(window, textvariable=t1, font=8)
e1.grid(row=1, column=15)

l3 = Label(window, text="DICTIONARY", bg="red", fg="black", font=56, padx=14, pady=14)
l3.grid(row=5, column=15)

Text_dict = Text(window, height=10, width=30, padx=10, pady=10, wrap=WORD)
Text_dict.grid(row=8, column=15, columnspan=4, rowspan=11)
Text_dict.insert(END, "The meaning of the entered word========>>>     ")


b4 = Button(window, text="New", bg="light blue", border=8, height=2, width=10, command=open_new)
b4.grid(row=4, column=15)


Text_main = Text(window, height=45, width=140, padx=10, pady=10, wrap=WORD, font=6)
Text_main.grid(row=0, column=0, columnspan=10, rowspan=35, sticky=N+E+W+S)


sb1 = Scrollbar(window)
sb1.grid(row=0, column=11, rowspan=35, sticky=N+S)

Text_main.configure(yscrollcommand=sb1.set)
sb1.configure(command=Text_main.yview)

window.mainloop()
