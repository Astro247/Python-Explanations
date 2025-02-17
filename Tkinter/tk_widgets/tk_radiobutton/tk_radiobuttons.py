#I radiobuttons sono un'insieme di checkbox con la caratteristica che puoi selezionarne solo una in una lista.

from tkinter import *

window = Tk()

ham = PhotoImage(file="ham_image.png")
pie = PhotoImage(file="pie_image.png")
pizza = PhotoImage(file="pizza_image.png")

food = ["pizza", "pie", "ham"]
food_images = [pizza, pie, ham]


#Con il ciclo sottostante il programma sta iterando per ogni elemento nella lista "food" assegnando ad essi uno specifico radiobutton
#Avendo creato una variabile assegnata come argomento keyword argument alla funzione Radiobutton, a quest'ultima viene assegnato un valore "True" o "False" che determina la selezione di tutti i checkbox della lista.
#Assegnando alla variabile creata, come keyword argument nella funzione Radiobutton, il contatore index, ora una volta che viene selezionato un'elemento viene solo selezionato quello nella posizione "index" nella lista.

print_order = ""

def get_order():
    global print_order
    if food_type.get()==0:
        print_order = "You ordered pizza"
    elif food_type.get()==1:
        print_order = "You ordered pie"
    else:
        print_order = "You ordered ham"
    
    show_text.config(text = print_order)
    show_text.pack()

food_type = IntVar()

for index, name in enumerate(food): #Associo a "index" l'indice della lista, numerico, mentre a "name" il nome dell'elemento nella lista

    radiobutton = Radiobutton(window, text=name, variable=food_type, value=index)

    radiobutton.config(font=("Trebuchet MS", 20, "bold"), padx=20, image = food_images[index], compound="right")
    radiobutton.pack()

    radiobutton.config(command=get_order)
    show_text = Label(window, text="")
    show_text.pack()


window.mainloop()