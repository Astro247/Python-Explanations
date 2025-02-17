#I bottoni sono dei widget che, una volta premuti, eseguono un blocco/riga di codice.
#Essendo la funzione Button() con un return, quest'ultima va assegnata ad una variabile e ad esso è necessario passare come positional argument il nome della variabile associato alla finestra e, se lo si desidera, come keyboard argument text assegnandolo a una stringa

from tkinter import *

window = Tk()
button = Button(window, text="This is a button")

#La funzione .config() permette la configurazione del pulsante appena creato
#E' possibile personalizzare, in ordine, il font, grandezza del testo e stile del testo richiamando il keyboard argument "font"
#Per modificare il colore di sfondo del pulsante basta utilizzare il keyboard argument "bg", mentre per modificare il colore del testo è sufficiente usare il keyboard argument "fg", assegnando ad essi un colore a parole, come "black", oppure con un codice Hex

button.config(font=("Fixedsys", 30, "italic"))
button.config(bg = "light blue")
button.config(fg = "black")

#Essendo che, una volta premuto il pulsante, quest'ultimo "cambia di texture", per modificare il colore del pulsante e del testo quando il pulsante è premuto basta utilizzare i keyboard arguments "activebackground" e "activeforeground"

button.config(activebackground="blue")
button.config(activeforeground="white")

#Per aggiungere un'immagine al pulsante è necessario eseguire tre passaggi:
#1) Importare l'immagine per poterla utilizzare nel codice come "nome_immagine.png/jpg", oppure selezionare la directory di quest'ultimo, come keyboard argument nella funzione PhotoImage() assegnata ad una variabile
#2) Nella funzione .config(), utilizzare il keyboard argument "image" assegnandogli il nome della variabile associata all'immagine
#3) Non fare nient'altro però sostituirà il testo con l'immagine, pertanto per muovere l'immagine da una parte del testo senza sovrascriverlo basta utilizzare il keyboard argument "compound", assegnandogli dove si vuole posizionare l'immagine rispetto al testo

finger_image = PhotoImage(file="finger_point.png")
button.config(image=finger_image)
button.config(compound="left")

#Per disabilitare un bottone, dunque per renderlo inutilizzabile, è necessario utilizzare il keyboard argument "state" e assegnargli "DISABLED", viceversa assegnargli "ACTIVE" per abilitarlo

button_disabled = Button(window, text="This button is disabled")
button_disabled.config(font=("Comic Sans MS", 20, "bold"))
button_disabled.config(state=DISABLED)
button_disabled.pack()

button_active = Button(window, text="This button is enabled")
button_active.config(font=("Comic Sans MS", 20, "bold"))
button_active.config(state=ACTIVE)
button_active.pack()

#Infine, per far sì che il bottone esegua una funzione è necessario passargli, alla funzione .config(), il keyboard argument "command" e assegnarglici una funzione.
#Di base tutto ciò che il bottone esegue viene stampato nel terminale, pertanto, se si vuole stampare nella finestra, è necessario usare un label

COUNT = 0


def increase_number():
    global COUNT
    COUNT += 1
    show_counting.config(text=COUNT)


button.config(command=increase_number)
show_counting = Label(window, text=COUNT, font=("Arial", 40))
show_counting.pack()
button.pack()

window.mainloop()