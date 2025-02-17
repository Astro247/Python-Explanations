#Per modificare la grandezza di una finestra si richiama la funzione .geometry("a x b"), dove "a" e "b" sono la lunghezza e altezza dei pixel della finestra

from tkinter import * 

window = Tk()
window.geometry("400x400")

#Per modificare il titolo della finestra si richiama la funzione .title("<Nome Titolo>")
  
window.title("First GUI")

#Per modificare l'immagine in alto a sinistra della finestra si devono seguire tre passaggi:
#1) Importare l'immagine per poterla richiamare con facilità senza dover specificare la directory di quest'ultima
#2) Salvare l'immagine importata in una variabile richiamando la funzione Photoimage(), passandogli il nome dell'immagine come keyboard argument: <Variabile> = PhotoImage(file="immagine.png")
#3) Richiamare la funzione .iconphoto(True,<Nome Variabile Contenente Immagine>).

icon = PhotoImage(file = "smile_face.png")
window.iconphoto(True,icon)

#Per modificare il background della finestra con un singolo colore ci sono due modi per poterlo fare, entrambi passando alla funzione ".config(backround='<Colore>')" un keyboard argument
#1) Passare il nome del colore desiderato, come: <Nome Finestra>.config(background = "gray")
#2) Passare il codice hex di un colore, come:  <Nome Finestra>.config(background = "#666b6b"), dove # indica che ciò che verrà scritto dopo è un codice di uno specifico colore

window.config(background="#666b6b")
window.mainloop()
