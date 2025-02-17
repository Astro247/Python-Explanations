#Un "text widget" è un'area di testo, inseribile in input, salvabile in una variabile

from tkinter import *
from tkinter import colorchooser, messagebox

def change_font_color():
    color = colorchooser.askcolor()

    text_area.config(fg=color[1])


def print_text():
    text = text_area.get("1.0", END) #Assegna alla variabile "text" come stringa tutto il contenuto dal primo carattere fino all'ultimo
    printed_text.config(state=NORMAL)

    printed_text.delete("1.0", END) #Cancella tutto il testo precedente presente nella text area "printed_text"
    printed_text.insert(END, text) #Inserisce nella text area "printed_text" il contenuto salvato nella variabile "text"

    printed_text.config(state=DISABLED)


def main():
    
    global text_area
    global input_area_label
    global input_area
    global text_window
    global buttons_area
    global printed_text

    text_window = Tk()

    text_area = Text(width=50, height=15, bg="#bababa")
    text_area.grid(row=2, column=1, padx=10, pady=10)

    text_area_label = Label(width = 30, text="Text Area", bg="black", fg="white", font = ("Courier", 15, "bold"))
    text_area_label.grid(row=1, column=1)

    printed_text = Text(width=50, height=15, bg="#bababa", state=DISABLED)
    printed_text.grid(row=2, column=4, padx=10, pady=10)

    printed_text_area_label = Label(width = 30, text="Printed Text Area", bg="black", fg="white", font = ("Courier", 15, "bold"))
    printed_text_area_label.grid(row=1, column=4) 

    buttons_area = Frame(text_window) #Crea un'area specifica, chiamata "buttons_area" dentro la finestra principale
    buttons_area.grid(row=2, column=2, rowspan=2, padx=10, pady=10)

    font_color = Button(buttons_area, text="Font Color", font=("Arial", 10, "bold"), width=10, activebackground="black", activeforeground="white", command=change_font_color)
    font_color.grid(row=2, column=2)

    print_button = Button(buttons_area, text="Print", font=("Arial", 10, "bold"), width=10, activebackground="black", activeforeground="white", command=print_text)
    print_button.grid(row=3, column=2)

    text_window.mainloop()

main()