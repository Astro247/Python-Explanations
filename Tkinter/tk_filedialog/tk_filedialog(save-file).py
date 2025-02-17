#Sempre con la funzione filedialog è possibile salvare un file.

from tkinter import *
from tkinter import filedialog


def save_text(text_area):
    text = text_area.get(1.0,END) #Copia quanto scritto nel Text e lo salva nella variabile "text", dal primo carattere (1.0) all'ultimo (END)
    text_file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=((("Text File"), (".txt")), (("HTML File"), (".html")), (("All Files"), (".*")))) #Chiede all'utente dove il file deve essere salvato, di base l'estensione è ".txt", ma con la funzione filetypes ne sono state aggiunte altre
                                         
    text_file.write(text) #Trascrive quanto salvato nella variabile "text" nel file appena selezionato/creato
    text_file.close() #Chiude il file aperto durante la trascrittura

def main():
    
    save_text_window = Tk()
    save_text_window.title("Text to be saved")

    text_area = Text(save_text_window, width=50, height=15, bg="#bababa")
    text_area.grid(row=2, column=1, padx=10, pady=5)
    
    buttons_area = Frame(save_text_window)
    buttons_area.grid(row=2, column=2, padx=10, pady=10)

    text_area_title = Label(width = 30, text="Text Area", bg="black", fg="white", font = ("Courier", 15, "bold"))
    text_area_title.grid(row=1, column=1)

    text_area_title = Label(width = 30, text="Text Area", bg="black", fg="white", font = ("Courier", 15, "bold"))
    text_area_title.grid(row=1, column=1)

    save_button = Button(buttons_area, font=("Arial", 10, "bold"), activebackground="black", activeforeground="white", text="Save", command=lambda:save_text(text_area))
    save_button.pack()


    save_text_window.mainloop()

main()