#La funzione Entry(), da assegnare ad una variabile, genera nel GUI una casella di testo nel quale è possibile scriverci in input qualsiasi cosa si desidera.

from tkinter import *

window_entry = Tk()
textbox = Entry()
textbox.pack()

#Per effettuare modifiche alla funzione entry è necessario richiamare la funzione .config()
#Per modificare il font, grandezza del font e stile del font è sufficiente passare alla funzione il keyboard argumet "font" e inserire i dati in ordine.

textbox.config(font=("Courier New", 30, "italic"))

#Per modificare il colore dello sfondo della casella di testo è sufficiente passare alla funzione il keyboard argument "bg" e inserire a parole o con un codice hex il colore desiderato.
#Il discorso si ripete per modificare il colore del testo, ma in questo caso il keyboard argument da passare alla funzione è "fg"

textbox.config(bg="Gray")
textbox.config(fg="Black")

#La funzione .insert() fa sì che sia già presente del testo ancora prima che questo venga scritto dall'utente. Alla funzione è necessario richiamare il positional argument posizione del testo, o indice del testo rappresentato da un numero, e il positional argument che rappresenta la stringa che apparirà nella casella di testo.

written_textbox = Entry()
written_textbox.insert(0,"Hello")
written_textbox.config(font=("Arial", 30, "bold"))
written_textbox.pack()

#Per disabilitare o abilitare una casella di testo è sufficiente passare alla funzione il keyboard argument "state" associandogli "DISABLED" per rendere inutilizzabile la casella di testo o "NORMAL" per abilitarla

disabled_textbox = Entry()
disabled_textbox.insert(0,"This textbox is disabled")
disabled_textbox.config(font=("Arial", 30, "bold"))
disabled_textbox.config(state=DISABLED)
disabled_textbox.pack()

enabled_textbox = Entry()
enabled_textbox.insert(0,"This textbox is enabled")
enabled_textbox.config(font=("Arial", 30, "bold"))
enabled_textbox.config(state=NORMAL)
enabled_textbox.pack()

#Per fare in modo che, indipendentemente dai caratteri inseriti in input, in output verrà mostrato a schermo un solo carattere è sufficiente passare alla funzione il keyboard argument "show" e assegnargli un carattere

hidden_textbox = Entry()
hidden_textbox.config(font=("Times New Roman", 40, "bold"))
hidden_textbox.config(show="*")
hidden_textbox.pack()

#La funzione "get", assegnata ad una variabile, salva il valore della stringa scritta in input nella casella di testo nella variabile.
#La funzione .delete() elimina una porzione di stringa inserita in input, ad essa devono essere passati i positional arguments "inizio" e "fine", ossia da dove a dove la stringa deve essere tagliata

def print_string():
    string = final_textbox.get()
    print.config(text="you printed: "+string)
    print.pack()


def delete_string():
    final_textbox.delete(0,END)


def backspace_one():
    final_textbox.delete(len(final_textbox.get())-1,END)


print= Label(window_entry, text="")
print.pack(side = BOTTOM)

print_button = Button(window_entry, text="print", command=print_string)
print_button.config(font=("Courier New", 10, "bold"))

delete_button = Button(window_entry, text="delete all", command=delete_string)
delete_button.config(font=("Courier New", 10, "bold"))

backspace_button = Button(window_entry, text="backspace", command=backspace_one)
backspace_button.config(font=("Courier New", 10, "bold"))

final_textbox = Entry()
final_textbox.pack(side=LEFT)
print_button.pack()
delete_button.pack()
backspace_button.pack()
final_textbox.config(font=("Arial", 30, "bold"))

window_entry.mainloop()