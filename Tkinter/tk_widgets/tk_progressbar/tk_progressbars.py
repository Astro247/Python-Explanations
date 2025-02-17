#Le Progressbar sono delle barre che si riempiono gradualmente nel momento in cui un'algoritmo, ad essa associato, viene completato

from tkinter import * #Importa la libreria tkinter
from tkinter import ttk #Importa una libreria secondaria di tkinter per più funzionalità
import time


def start_download(progress_bar, download_window, show_current_operation, download_button):

    download_button.config(state=DISABLED) #Disabilita il pulsante una volta premuto

    operations = 100
    current_operation = 0
    
    while(current_operation<operations):
        time.sleep(0.05) #Fa sì che fra un operazione e l'altra ci sia un ritardo di 0.05 secondi, non rendendo tutto istantaneo
        progress_bar['value']+=1 #Il valore della barra di progresso viene aumentato di 1 ad ogni iterazione (con un massimo di 100)

        current_operation+=1
        show_current_operation.set(f"{current_operation}/100 Operation Completed") #La variabile "show_current_operation" viene aggiornata con una nuova stringa ad ogni iterazione
        
        download_window.update_idletasks() #L'intera finestra viene aggiornata al fine del ciclo, se così non fosse la finestra verrebbe aggiornata solo quando il caricamento è finito del tutto
    

def main():

    download_window = Tk()
    download_window.title("Download")
    
    progress_bar = ttk.Progressbar(download_window, length=300, orient=HORIZONTAL) #Con la libreria ttk viene creata una Progressbar, con una lunghezza di 300 e un orientamento orizzontale.
    progress_bar.pack(padx=5, pady=5)

    show_current_operation = StringVar() #Una StringVar è un tipo di variabile associata ai widgets con un testo da aggiornare con il tempo
    show_progress = Label(download_window, textvariable=show_current_operation, font=("Arial", 10, "bold")) #Il keyword argument textvariable fa sì che, come testo, venga considerato il valore di una variabile e non una stringa fissa come per il keyword argument "text"
    show_progress.pack()

    download_button = Button(download_window, text="Start Download", font=("Arial", 12, "bold"), bg="#808080", activebackground="black", activeforeground="white")
    download_button.config(command=lambda:start_download(progress_bar, download_window, show_current_operation, download_button))
    download_button.pack(padx=5, pady=5)

    download_window.mainloop()

main()
