#Un checkbox è una casella nella quale, cliccandoci, una spunta riempirà la casella che a sua volta eseguirà una funzione.
#La funzione Checkbutton() passa alla funzione il positional argument nome della finestra e come keyword argument il testo "text" associato alla stringa da stampare accanto al checkbox.
#Alla funzione inoltre possono essere passati i keyword arguments "variable" che assegna il check o meno della casella al valore di una variabile, "onvalue" e "offvalue" che assegnano uno specifico valore alla variabile qualora il check sia off oppure on e "command", ossia la funzione da eseguira se onvalue ritorna un valore booleano True.

from tkinter import *

output_text = ""


def test():
    global output_text

    if check.get()==1:
        output_text = "You checked the box"
    if check.get()==0:
        output_text = "You removed the check from the box"
    
    show_text.config(text=output_text)


window_checkbox = Tk()
window_checkbox.geometry("250x100")
check = IntVar() #definisce la variabile check come intero

checkbox = Checkbutton(window_checkbox, text="This is a test", variable=check, onvalue=1, offvalue=0, command=test) 

#Nel codice sottostante con la funzione .config e gli argomenti "font", "bg" e "fg" viene modificata l'area di testo

checkbox.config(font=("Helvetica", 20))
checkbox.config(bg="Black", activebackground="Black")
checkbox.config(fg="White", activeforeground="White")

#Con la funzione PhotoImage() viene aggiunta un'immagine accanto al testo

coffee_cup = PhotoImage(file="coffee_cup.png")
checkbox.config(image=coffee_cup, compound="right")

show_text = Label(window_checkbox, text="")
show_text.config(font=("Times New Roman", 10))
checkbox.pack()
show_text.pack()




window_checkbox.mainloop()