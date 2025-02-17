#Le listbox sono delle liste rappresentate in tkinter, pertanto ogni elemento della lista possiede un suo specifico indice.

from tkinter import *

listbox_window = Tk()
listbox_window.title("Menù")


def select_item(selected_menù_items, selected_menù, menù, price):

    food_without_price = menù.get(menù.curselection()).rsplit(" ", 1)[0] #La funzione menù.curselection() crea una tupla nella quale viene salvato l'indice dell'elemento selezionato con il mouse, mentre la funzione .rsplit(" ", 1)[0] divide la stringa, in questo caso il nome del cibo, in un punto, creando dunque una lista con massimo due elementi ossia le due parti della stringa, nel momento in cui incontra il carattere " ", effettuando questo controllo partendo da destra, selezionando poi in quella lista creata l'elemento con indice [0], ossia il nome del cibo in questo caso 
    selected_food = menù.get(menù.curselection())

    full_food_price = menù.get(menù.curselection()).rsplit(" ", 1)[1] #assegno alla variabile full_food_price la parte di stringa selezionata che contiene solo il prezzo 
    number_price = full_food_price.replace("$", "") #assegno alla variabile number_price solo il numero, eliminando il carattere "$"

    present_value = 0

    for food in selected_menù_items:
        if selected_food == food:
            present_value = 1

    if present_value == 0:
        selected_menù_items.append(selected_food)
        price.append(number_price)
        selected_menù.insert(END, food_without_price)


def delete_item(selected_menù_items, selected_menù, price): #Funzione per cancellare un'elemento dalla listbox 

    item_to_remove = selected_menù.curselection() 
    del selected_menù_items[item_to_remove[0]]

    price_to_remove = selected_menù.curselection()
    del price[price_to_remove[0]]

    for index in item_to_remove: 
        selected_menù.delete(index)
        

def get_final_price(menù, selected_menù, price):

    final_price = 0

    for single_price in price:
        final_price = final_price + int(single_price)

    print_final_label(menù, selected_menù,final_price)


def print_final_label(menù, selected_menù, final_price):

    menù.config(state=DISABLED)
    selected_menù.config(state=DISABLED)
    select_button.config(state=DISABLED)
    delete_button.config(state=DISABLED)
    done_button.config(state=DISABLED)

    final_text = f"Thank you for your purchase!\n The total price is: {final_price}$"

    total_cost.config(text=final_text)
        

menù_title = Label(listbox_window, text = "Menù", relief=RAISED, bg = "#b3b2ad", fg = "black", width = 20, font = ("Arial", 15, "italic"))
menù_title.grid(row=1, column=1)

selected_menù_title = Label(listbox_window, text = "Selected Menù", relief=RAISED, bg = "#b3b2ad", fg = "black", width = 20, font = ("Arial", 15, "italic"))
selected_menù_title.grid(row=1, column=2, columnspan=3)

total_cost = Label(listbox_window, relief=RAISED, font=("Courier New", 15, "bold"), width = 30)
total_cost.grid(row=4, column=1, columnspan=4, pady=5)

menù_items = [("Pizza Slice", 2), ("Pasta", 5), ("Salad", 3), ("Sandwich", 2), ("Salmon", 10), ("Beef", 15), ("Skewers", 8), ("Water Bottle", 1)]
selected_menù_items = []
price = []


menù = Listbox(listbox_window, bg = "gray", fg = "white", width = 22, font = ("Arial", 15, "bold"))
for name, single_price in menù_items:
    item_listbox = f"{name} {single_price}$"
    menù.insert(END, item_listbox) #Inserendo "itembox", contenente il nome, contatore name del ciclo for rappresentante la stringa nella tuple, e il prezzo, ossia il contatore price rappresentante l'intero nella tuple.    
menù.grid(row=2, column=1, padx=15)

selected_menù = Listbox(listbox_window, bg = "gray", fg = "white", width = 22, font = ("Arial", 15, "bold"))
selected_menù.grid(row=2, column=2, columnspan=3, padx=15)

select_button = Button(listbox_window, text="Select", font = ("Arial", 10, "bold"), width=10, bg = "#bfbcbb", activebackground = "#918f8e")
select_button.config(command=lambda: select_item(selected_menù_items, selected_menù, menù, price))
select_button.grid(row=3, column=1, pady=2)

delete_button = Button(listbox_window, text="Delete", font = ("Arial", 10, "bold"), width=10, bg = "#bfbcbb", activebackground = "#918f8e")
delete_button.config(command=lambda: delete_item(selected_menù_items, selected_menù, price))
delete_button.grid(row=3, column=2, pady=2)

done_button = Button(listbox_window, text="Done", font = ("Arial", 10, "bold"), width=10, bg = "#bfbcbb", activebackground = "#918f8e")
done_button.config(command=lambda: get_final_price(menù, selected_menù, price))
done_button.grid(row=3, column=3, pady=2)

listbox_window.mainloop()