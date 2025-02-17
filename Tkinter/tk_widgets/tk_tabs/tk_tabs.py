#Le tabs in python sono considerabili come finestre differenti racchiuse in un'unica finestra.
#Per accedere a più tab è necessaria la libreria "ttk"
#Tutte le nuove tab create non sono altro che dei Frame alla quale gli viene passato, come positional argument, la variabile associata alla funzione Notebook (che gestisce le diverse tabs)
#In quato Frame, tutte le tab create vengono utilizzate esattamente come se fossero finestre separate da quella principale.

from tkinter import *
from tkinter import ttk

notebook_window = Tk()

tabs_manager = ttk.Notebook(notebook_window) #alla variabile "tabs_manager" gli è ora associata la gestione delle diverse tabs

labels_tab = Frame(tabs_manager) #Crea la prima tab
buttons_tab = Frame(tabs_manager) #Crea la seconda tab

tabs_manager.add(labels_tab, text="Labels Tab") #Aggiunge i frame creati
tabs_manager.add(buttons_tab, text="Buttons Tab")
tabs_manager.pack(expand=True, fill="both") #La funzione expand, settata a True, fa sì che, indipendentemente dal ridimensionamento della finestra, il frame con in alto le tab rimanga sempre al centro
                                            #La funzione "fill", settabile sull'asse x, y o entrambi (both), fa sì che indipendentemente dalla scale della finestra, il frame con le tab rimane sempre nella stessa posizione
hello_label = Label(labels_tab, text="Hello", font=("Georgia", 20, "bold"), relief=RAISED, bg="#3e8761", fg="#102254")
hello_label.pack(expand=True)

how_are_you_button = Button(buttons_tab, text="How are you?", font=("Georgia", 20, "bold"), bg="#9e9b3e", fg="#52226b", activebackground="#666430")
how_are_you_button.pack(expand=True)


notebook_window.mainloop()