#Spostare i widget all'interno di un frame è fattibile con la creazione di un'algoritmo specifico, non ci sono funzioni singole specifiche che permettono ciò.

from tkinter import *


def save_initial_coordinates(event):
    widget = event.widget #Ottiene il riferimento al widget su cui si è verificato l'evento (in altre parole capisce a quale widget ci stiamo riferendo)
    
    widget.startX = event.x #Salva la coordinata x iniziale del widget selezionato
    widget.startY = event.y #Salva la coordinata y iniziale del widget selezionato


def drag_widget(event):
    widget = event.widget  
    parent = widget.master  #Scrivendo widget.master, alla variabile parent viene assegnato il Frame che contiene quel Label.

    frame_width = parent.winfo_width() #Assegna alla variaibile locale frame_width il width del Frame parent.
    frame_height = parent.winfo_height() #Assegna alla variaibile locale frame_height il height del Frame parent.
 
    widget_width = widget.winfo_width() #Assegna alla variabile widget_width il width del widget selezionato dal mouse.
    widget_height = widget.winfo_height() #Assegna alla variabile widget.height il height del widget selezionato dal mouse.

    new_x = widget.winfo_x() - widget.startX + event.x #Aggiorna la coordinata x del widget dinamicamente, ossia man mano che esso viene spostato nel frame
    new_y = widget.winfo_y() - widget.startY + event.y #Aggiorna la coordinata y del widget dinamicamente

    # Controllo per evitare che il widget esca dal frame
    if new_x < 0:
        new_x = 0
    elif new_x + widget_width > frame_width:
        new_x = frame_width - widget_width

    if new_y < 0:
        new_y = 0
    elif new_y + widget_height > frame_height:
        new_y = frame_height - widget_height

    for other_widget in parent.winfo_children():  #Cicla nel frame parent cercando tutti i widget presenti (ossia i figli del loro contenitore padre, cioè "parent")
        if other_widget == widget:  #Evita il widget selezionato dal mouse
            continue

        other_x = other_widget.winfo_x() #Salva le coordinate x degli altri widget
        other_y = other_widget.winfo_y() #Salva le coordinate y degli altri widget

        other_width = other_widget.winfo_width() #Salva il width degli altri widget
        other_height = other_widget.winfo_height() #Salva il height degli altri widget

        if (new_x < other_x + other_width and new_x + widget_width > other_x and new_y < other_y + other_height and new_y + widget_height > other_y): #Controlla se il widget in movimento con il mouse si sovrappone con gli altri widget nel frame parent
            return #Se i widget si sovrappongono, allora la funzione si chiude, interrompendo il movimento del widget selezionato fino al prossimo click del mouse
        
    widget.place(x=new_x, y=new_y) #Posiziona il widget nelle coordinate finali


def main():

    drag_widgets_window = Tk()
    drag_widgets_window.title("Drag Widgets")

    one_widget_label = Label(drag_widgets_window, text="Single Widget", bg="Black", fg="white", font=("Arial"))
    one_widget_label.grid(row=1, column=1, sticky="nsew", padx=10)

    two_widgets_label = Label(drag_widgets_window, text="Double Widgets", bg="Black", fg="white", font=("Arial"))
    two_widgets_label.grid(row=1, column=2, sticky="nsew", padx=10)

    one_widget_frame = Frame(drag_widgets_window, height=250, width=250, bg="gray")
    one_widget_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    two_widget_frame = Frame(drag_widgets_window, height=250, width=250, bg="gray")
    two_widget_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    single_widget = Label(one_widget_frame, bg="red", width=10, height=5, relief=RAISED, bd=5)
    single_widget.place(x=0,y=0)

    single_widget.bind("<Button-1>", save_initial_coordinates) #Al premere del tasto destro viene richiamata la funzione save_initial_coordinates
    single_widget.bind("<B1-Motion>", drag_widget) #Tenendo premuto il tasto sinistro viene richiamata la seconda funzione

    double_widget_red = Label(two_widget_frame, bg="red", width=10, height=5, relief=RAISED, bd=5)
    double_widget_red.place(x=0,y=0)

    double_widget_red.bind("<Button-1>", save_initial_coordinates)
    double_widget_red.bind("<B1-Motion>", drag_widget)

    double_widget_blue = Label(two_widget_frame, bg="blue", width=10, height=5, relief=RAISED, bd=5)
    double_widget_blue.place(x=150,y=0)

    double_widget_blue.bind("<Button-1>", save_initial_coordinates)
    double_widget_blue.bind("<B1-Motion>", drag_widget)

    drag_widgets_window.mainloop()

main()


