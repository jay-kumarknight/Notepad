import json
from tkinter import *
import tkinter.messagebox
from difflib import get_close_matches


data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        output = data[w]
        if type(output) == list:
            for item in output:
                return item
        else:
            return output

    elif w.title() in data:
        output = data[w.title()]
        if type(output) == list:
            for item in output:
                return item
        else:
            return output

    elif w.upper() in data:
        output = data[w.upper()]
        if type(output) == list:
            for item in output:
                return item
        else:
            return output

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = tkinter.messagebox.askquestion("Warning", "Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
        if yn == "yes":
            output = data[get_close_matches(w, data.keys())[0]]
            if type(output) == list:
                for item in output:
                    return item
            else:
                return output

        elif yn == "no":
            tkinter.messagebox.showinfo("CHECK", "The word doesn't exist. Please double check it.")
        else:
            tkinter.messagebox.showinfo("CHECK", "We didn't understand your entry.")
    else:
        tkinter.messagebox.showinfo("WARNING", "The word doesn't exist. Please double check it.")
