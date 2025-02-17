#WARNING: DO NOT RUN THIS CODE IF YOU DON'T KNOW HOW TO STOP IT IN OTHER WAYS

#Un messagebox è una finestra di errore, info o warning che può ritornare un valore booleano oppure una stringa. E' importante specificare la funzione da importare nel codice

from tkinter import *
from tkinter import messagebox
import random

messagebox_window = Tk()
messagebox_window.title("This is not a virus")

#Esistono due tipi di messagebox: I "message ask box", che chiedono all'utente una risposta, ed i "message info/warning/error box", che segnalano qualcosa all'utente permettendogli solo di rispondere "ok"

def error_box():
    messagebox.showerror(title="fatal error", message="wrong answer >:(")

#Esistono diversi tipi di "message ask box", il loro funzionamento è specificato nel nome della funzione, tutto ciò che è nominato con un "yesno", quest'ultima ritorna la stringa "yes" oppure "no" (se si parla di yesnocancel allora potrebbe ritornare anche la stringa "none")
#Tutto il resto ritorna una variabile booleana

def show_random_errors():
    while True:
        print("FATAL ERROR: Y O U   D O N ' T   L I K E   M E")
        error_label = Label(messagebox_window, bg="red",fg="black", font=("Arial", 15, "bold"), text="FATAL ERROR")
        error_label.pack()
        messagebox.showerror(title="FATAL ERROR", message="Y O U   D O N ' T   L I K E   M E")

        

def second_no_choice():
    messagebox.showwarning(title=".", message=".")
    messagebox.showwarning(title=".", message="ok.")
    messagebox.showwarning(title=".", message="I'm giving you one chance to take it back.")
    
    answer = messagebox.askretrycancel(title=".", message="you don't want to re-insert a different answer?",)
    if answer:
        new_answer = messagebox.askquestion(title="?", message="So, do you like me?")
        if new_answer == "yes":
            messagebox.showinfo(title=".", message="better.")
        else:
            show_random_errors()
    else:
        show_random_errors()


def first_no_choice():
    messagebox.showwarning(title="!", message="what??")
    messagebox.showwarning(title="!..", message="oh wait")
    messagebox.showwarning(title="?", message="maybe you mistakenly pressed the wrong button")
    messagebox.showwarning(title="?", message="it's ok, it can happend sometimes")
    
    answer = messagebox.askquestion(title="?", message="So, do you like me?")

    if answer == "yes":
        messagebox.showinfo(title=":)", message="see? I knew you just missclicked!")
    else:
        second_no_choice()

def ask_yes_no():

    answer = messagebox.askquestion(title="?", message="do you like me? =)")

    if answer == "yes":
        messagebox.showinfo(title=":)", message="thank you :)")
    else:
        first_no_choice()





click_me_button = Button(messagebox_window, text="Click me :)", width=15, font=("Arial", 20, "bold"), bg="gray", activebackground="black", fg="black", activeforeground="white")
click_me_button.config(command=ask_yes_no)
click_me_button.pack(pady=10, padx=10)        

messagebox_window.mainloop()