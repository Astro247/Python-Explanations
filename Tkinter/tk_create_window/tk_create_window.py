#Tkinter è una libreria utile per creare "GUI", ossia finestre interattive, importata interamente a riga 3, richiamabile semplificatamente come "tk"

import tkinter as tk #Dato che stiamo importando tutto, sarebbe andato bene anche: from tkinter import *

#Per creare una finestra si richiama la funzione .Tk() e viene assegnata ad una variabile

window = tk.Tk()

#Nonostante la finestra è stata creata, una volta aperta si chiude automaticamente, poiché è pur sempre un programma che si apre e si chiude una volta terminato.
#Per risolvere questo problema si richiama la funzione <Nome Finestra>.mainloop(), la quale fa sì che il programma entri in un ciclo while infinito per lasaciare la finestra aperta.

window.mainloop()
