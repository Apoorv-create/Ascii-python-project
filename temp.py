# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx = 0.5,rely = 0.4, anchor=CENTER)

label = Label(root, text = "name in Ascii :", bg="light yellow", fg="black")

def asciiconverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
    
btn = Button(root, text = "show me in ascii", command=asciiconverter, bg="gold", fg="black")    
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()