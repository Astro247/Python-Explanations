#La funzione filedialog fa sì che, nel codice, sia possibile gestire l'apertura di un file e di poterlo salvare.

from tkinter import *
from tkinter import filedialog #funzione da importare a parte

filedialog_window = Tk()
filedialog_window.title("filedialog")

first_file_directory = ""

def get_direcotry_file():
    global first_file_directory
    first_file_directory = filedialog.askopenfilename(title="Get Directory", filetypes=(("text files", "*.txt"), ("all files", "*.*"))) #Salva la directory in una variabile. il keyword argument "filetypes" fa sì che possano essere ricercati determinati file, si assegna, fra parentesi, il nome per un tipo di file da ricercare e il tipo di file (per esempio *.txt fa sì che vengano rintracciati solo i file txt, mentre *.* tutti i file).

    directory_text = f"Directory = {first_file_directory}"
    show_directory_label.config(text=directory_text)


def get_file_content():
    file_directory = filedialog.askopenfilename(title="Get File Content") #Salva la directory in una variabile
    file = open(file_directory, 'r') #Il file viene aperto con la funzione open in modalità solo lettura, quindi non può essere modificabile ma solo leggibile, e salvato in una variabile
    
    show_content_label.config(text=file.read()) #Aggiorna il label salvando in esso il contenuto del file con la funzione .read()
    file.close() #Una volta fatto, il file viene chiuso con la funzione .close()
    

def open_previous_directory():
    global first_file_directory
    filedialog.askopenfilename(initialdir=first_file_directory, title = "Previous Directory")


get_direcotry_button = Button(filedialog_window, text="Get Directory", font = ("Arial", 15, "bold"), command = get_direcotry_file)
get_direcotry_button.grid(row=1, column=1)

show_directory_label = Label(filedialog_window, font = ("Arial", 15, "bold"), bg="#a8a7a5", fg="black")
show_directory_label.grid(row=1, column=2)

get_content_button = Button(filedialog_window, text="Get Content", font = ("Arial", 15, "bold"), command = get_file_content)
get_content_button.grid(row=2, column=1)

show_content_label = Label(filedialog_window, font = ("Arial", 15, "bold"), bg="#a8a7a5", fg="black")
show_content_label.grid(row=2, column=2)

saved_directory_button = Button(filedialog_window, text="Re-open Previous Directory", font = ("Arial", 15, "bold"), command = open_previous_directory)
saved_directory_button.grid(row=3, column=1)


filedialog_window.mainloop()