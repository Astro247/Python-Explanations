#La funzione .bind fa sì che i tasti della tastiera vengano considerati come dei Button, pertanto una volta premuti richiamano una funzione.

from tkinter import *


def show_pressed_key(w_key, show_key, event):

    if str(event.keysym) == "w": #event.keysym si riferisce al tasto premuto in input da tastiera
        w_key.config(text="you pressed 'W'")

    else:
        w_key.config(text="you didn't press 'W'")

    show_key.config(text=event.keysym) 


def main():

    bind_window = Tk()
    bind_window.title("Key Shown")

    w_key_label = Label(bind_window, text="Press 'W' to trigger a function: ", font=("Arial", 20, "bold"), relief=RAISED, bd=5, bg="#c1e38f", fg="black", width=25)
    w_key_label.grid(row=1, column=1)
    
    w_key = Label(bind_window, font=("Arial", 20, "bold"))
    w_key.grid(row=1, column=2)

    show_key_label = Label(bind_window, text="Key Pressed: ", font=("Arial", 20, "bold"), relief=RAISED, bd=5, bg="#ac8fe3", fg="black", width = 25)
    show_key_label.grid(row=2, column=1)

    show_key = Label(bind_window, font=("Arial", 20, "bold"))
    show_key.grid(row=2, column=2)

    bind_window.bind("<Key>", lambda event: show_pressed_key(w_key, show_key, event)) #Necessario passare l'argomento "event", inoltre il tasto "<Key>" si riferisce a qualsiasi input da tastiera

    bind_window.mainloop()

main()