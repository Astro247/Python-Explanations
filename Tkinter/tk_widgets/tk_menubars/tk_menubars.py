#I menubars sono dei menù comodi da usare alla quale, per ogni menù, viene passato degli specifici comandi e ad essi delle funzioni.

from tkinter import *
from tkinter import filedialog, messagebox, colorchooser


def open_text(text_area):
    file_directory = filedialog.askopenfilename(title="Open File", defaultextension=".txt", filetypes=((("Text Files"), (".txt")), (("All Files"), (".*")))) #Chiede all'utente di selezionare un file .txt
    if not file_directory:  #Se l'utente non ha selezionato alcun file non darà errore
        return

    answer = messagebox.askyesno(title="Warining", message="The current text will be overwritten, do you want to continue?")
    if answer:
        text_file = open(file_directory, "r") #Una volta selezionato, il file viene aperto in quella specifica path in modalità solo lettura
        text_area.delete("1.0", END) #Il testo precedente nel Text viene rimpiazzato con il file aperto

        text_copied = text_file.read() #Il file aperto viene letto e "trascritto" nella variabile text_copied
        text_area.insert(END, text_copied) #Il contenuto della variabiile text_copied viene inserito nel Text come modificabile
        text_file.close() #Il file aperto viene chiuso 


def save_text(text_area):
    chosen_file = filedialog.asksaveasfile(title="Save File", defaultextension=".txt", filetypes=((("Text Files"), (".txt")), (("All Files"), (".*")))) #Chiede all'utente di selezionare un file .txt nella quale verrà salvato il contenuto del Text
    text_content = text_area.get(1.0, END) #Il contenuto del Text viene salvato dal primo carattere fino all'ultimo nella variabile "text_content"

    chosen_file.write(text_content) #Nel file selezionato/creato dall'utente gli viene copiato quanto scritto nel Text
    chosen_file.close() #Il file viene chiuso


def exit_program(menu_bars_window):
    answer = messagebox.askyesno(title="Exiting", message="Are you sure you want to exit?")

    if answer:
        menu_bars_window.quit() #La finestra principale viene chiusa


def change_text_color(text_area):
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])
  

def main():

    menu_bars_window = Tk()
    menu_bars_window.title("Editable Text")

    exit_icon = PhotoImage(file="exit_icon.png")
    open_icon = PhotoImage(file="open_icon.png")
    save_icon = PhotoImage(file="save_icon.png")
    modify_color_icon = PhotoImage(file="modify_color_icon.png")

    text_area = Text(menu_bars_window, height=15, width=50, bg="gray")
    text_area.pack(padx=10, pady=10)

    menu_bar = Menu(menu_bars_window) #Viene creata una barra per i diversi menù nella finestra principale
    menu_bars_window.config(menu=menu_bar) #Il menù creato viene mostrato a schermo

    file_menu = Menu(menu_bar, tearoff=0) #Nella variabile "file_menu", ossia un ulteriore menù non dentro la finestra principale, ma dentro il menù creato precedentemente, vengono poi salvate delle fuzionalità. Il keyword argument "tearoff" è assegnnato a zero in quanto questo elimina una linea di default presente fra le fuzionalità di "file_menu"
    menu_bar.add_cascade(label="File", menu=file_menu) #Fa sì che il menù sia a cascata, quindi una olta premuto il tasto "File" nel menù quest'ultimo apre le funzionalità di "file_menu" una sotto l'altra
    file_menu.add_command(label="Open ", font=("Arial", 15), image=open_icon, compound="right", command=lambda:open_text(text_area)) #Viene aggiunto un comando fra le funzionalità di "file_menu"
    file_menu.add_command(label="Save ", font=("Arial", 15), image=save_icon, compound="right", command=lambda:save_text(text_area)) #Viene aggiunto un comando fra le funzionalità di "file_menu"
    file_menu.add_separator() #Aggiunge una linea di separazione
    file_menu.add_command(label="Exit ", font=("Arial", 15), image=exit_icon, compound="right", command=lambda:exit_program(menu_bars_window)) #Viene aggiunto un comando fra le funzionalità di "file_menu"

    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Change Text Color", font=("Arial", 15), image=modify_color_icon, compound="right", command=lambda:change_text_color(text_area))
    menu_bars_window.mainloop()
    
main()