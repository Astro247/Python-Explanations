#La funzione Label permette l'aggiunta di widgets come testo o immagini al GUI.
#In quanto la funzione Label ha un return, è necessario assegnarlo ad una variabile, per poi passare alla funzione la variabile positional argument assegnata al nome della finestra e il keyboard argument "text" assegnandogli una stringa a piacimento.
#Dopo aver creato il label, per aggiungerlo alla finestra è necessario specificare la posizione dove quest'ultimo verrà aggiunto, per farlo ci sono diversi modi, i più semplici sono:
#1) Dopo aver dichiarato il label richiammare la funzione .pack() che automaticamente posiziona il label al centro in alto nel GUI, mettendo a capo altri label futuri.
#2) Impostando la posizione manualmente del testo con una coppia coordinate x e y, le quali rappresentano i pixel occupati nel GUI, richiamando la funzione .place() dove lo zero di entrambi è in alto a sinistra.

from tkinter import *

window = Tk()

text_pack = Label(window, text="This is a text positioned with the function '.pack()'")
text_pack.pack()

text_coordinates = Label(window, text="This is a text positioned with coordinates")
text_coordinates.place(x=50,y=50)


#Per modificare il font del testo, una volta passato il keyboard argument "text", è necessario passare alla funzione un'ulteriore keyboard argument "font", alla quale vengono assegnati in ordine: tipo di font, grandezza del testo e stile del font.

modified_text = Label(window, 
                      text="This text is modified", 
                      font=("Comic Sans MS", 40, "bold"))
modified_text.pack()

#Per modificare il colore del testo è necessario passare alla funzione il keyboard argument "fg", assegnandogli a parole il colore desiderato oppure inserendo un codice Hex
#Per personalizzare il colore dell'area occupata da un testo si passa alla funzione il keyboard argument "bg", come per il keyboard argument "fg", si assegna a quest'ultimo il colore a parole o con un codice Hex

colorful_text = Label(window, 
                      text="this text is colorful", 
                      font=("Arial", 30, "bold"), 
                      fg="green", 
                      bg="black")
colorful_text.pack()

#Per aggiungere una riquadro al testo, ossia una linea di separazione fra il colore del keyboard argument "bg" e il resto della finestra, è necessario passare alla funzione il keyboard argument "relief", assegnandoci il tipo di riquadro che si desidera.
#Per determinare lo spessore del riquadro, alla funzione è necessario passargli il keyboard argument "bd", assegnandogli il numero di pixel che il riquadro andrà ad occupare.
#E' inoltre possibile determinare il numero di pixel che separano il testo dal riquadro passando alla funzione i keyboard arguments "padx", alla quale viene assegnato il numero di pixel che separano i due orizzontalmente, e "pady", alla quale viene assegnato il numero di pixel che separano i due verticalmente.

boxed_text = Label(window, 
                   text="This text is boxed", 
                   font=("Arial", 30, "bold"), 
                   fg="white", bg="blue", 
                   relief=RAISED, 
                   bd=15, 
                   padx=10, 
                   pady=10)
boxed_text.pack()

#Per stampare un'immagine a schermo si devono seguire due passaggi:
#1) Prima di tutto è necessario aggiungere l'immagine nel codice per poterla utilizzare, questo si fa utilizzando la funzione PhotoImage che, in quanto possiede un return, va assegnata ad una variabile, specificandone con il keyboard argument "file" la directory oppure se è nella stessa cartella del programma specificarne solo il nome
#2) passare alla funzione Label il keyboard argument "image", assegnandogli il nome della variabile assegnata alla funzione PhotoImage.

planet_image = PhotoImage(file="planet.png")

image = Label(window, 
              image=planet_image, 
              relief=RAISED, 
              bd=15)
image.pack()

#Infine, per inserire sia del testo che un'immagine è necessario passare alla funzione il keyboard argument "compound", assegnandogli a parole la posizione dell'immagine rispetto al testo (come bottom, left, right o above)

image_text = Label(window, 
                   text="This Text is next to an image", 
                   font=("Fixedsys", 40, "bold"), 
                   fg="white", 
                   bg="black", 
                   relief=RAISED, 
                   bd=15, 
                   padx=10, 
                   pady=10, 
                   image = planet_image,
                   compound="right")
image_text.pack()

window.mainloop()