#La funzione colorchooser permette all'utente di inserire manualmente un colore in input per qualcosa di specifico.

from tkinter import *
from tkinter import colorchooser


def change_color():

    color = colorchooser.askcolor() #Apre una tab che permette all'utente di scegliere un colore e quest'ultimo, se assegnato ad una variabile, rende quest'ultima una lista contenente l'RGB del colore e il suo codice hex

    current_rgb_color = f"Curret RGB code: {color[0]}"
    current_hex_color = f"Current Hex code: {color[1]}"

    rgb_code_color.config(text=current_rgb_color)
    hex_color.config(text=current_hex_color)

    colorchooser_window.config(bg=color[1]) #Assegno come colore background della finestra il colore preso in input assegnato alla variabile "color"



colorchooser_window = Tk()

color_button = Button(colorchooser_window, width = 15, text="here", command=change_color)
color_button.grid(row=1, column=2, pady=10, padx=10)

text_label = Label(colorchooser_window, font=("Arial", 15, "bold"), text="press this button to change color →", bg="white")
text_label.grid(row=1, column=1, pady=10, padx=10)

rgb_code_color = Label(colorchooser_window, font=("Arial", 15, "bold"), bg="white")
rgb_code_color.grid(row=2, column=1, pady=10, padx=10)

hex_color = Label(colorchooser_window, font=("Arial", 15, "bold"), bg="white")
hex_color.grid(row=3, column=1, pady=10, padx=10)

colorchooser_window.mainloop()
