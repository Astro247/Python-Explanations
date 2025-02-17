#Canvases è una funzione che permette di creare, all'interno del GUI, figure geometriche semplici o grafici.

from tkinter import *


def main():

    geometry_window = Tk()
    geometry_window.title("Simple Geometry")

    simple_figures = Canvas(geometry_window, width=500, height=500) #Alla variabile "simple_figures" è stata assegnata la funzione Canvas, dunque adesso la variabile rappresenta un'area nella quale le coordinate x sono specificate dalla width (in alto da sinistra a destra), mentre le coordinate y dalla height (dall'alto a sinistra al basso a sinistra)

    red_line_points = [0, 0, 500, 500] #Coordinate x e y associate ai due punti che creano la linea rossa (i primi due numeri rappresentano coordinate x e y del primo punto, mentre gli altri due le coordinate del secondo)
    simple_figures.create_line(red_line_points, fill="red", width=5, tags="red_line") #La funzione .create_line crea una linea semplice con due estremi, le cui coordinate sono passate come come positional argument, il keyword argument "fill" associato al nome di un colore o ad un codice hex che rappresenta il colore della figura, il keyword argument "width" che rappresenta il suo spessore e infine il keyword argument "tags" permette di assegnare alla figura appena creata un nome, riutilizzabile in seguito.

    blue_line_points = [35, 0, 25, 500]
    simple_figures.create_line(blue_line_points, fill="blue", width=5, tags="blue_line") 

    rectangle_points = [250, 5, 350, 350] #Per i rettangoli, bastano due coppie coordinate che rappresentano i punti della diagonale sulla quale poi si costruisce l'intera figura.
    simple_figures.create_rectangle(rectangle_points, width=3)
    points_show_rectangle = [250, 5, 350, 350]
    simple_figures.create_line(points_show_rectangle, width=3)

    triangle_points = [50, 250, 25, 300, 75, 300]
    simple_figures.create_polygon(triangle_points, width=5) #La funzionne .create_polygon permette di creare qualsiasi tipo di figura dipendentemente da quante coppie coordinate vengono fornite.

    #La funzione ".create_arc" permette la creazione di semi-circonferenze, come positional argument prende le coordinate dei punti della retta secante che attraverserebbe l'intero cerchio, ma quest'ultima non potrà estendersi di più del quadrato che circoscrive la circonferenza
    #Ci sono diversi keyword argument "style" passabili alla funzione ".create_arc", come "CHORD", che divide la semi-circonferenza da una corda, un segmento che come estremi prende i punti estremi alla circonferenza, eliminando l'area interna del cerchio.
    #Il keyword argument "ARC", invece, si limita a mostrare solo i punti alla circonferenza della semi-circonferenza.

    points_semi_circumference = [5, 5, 200, 200] #Coordinate della secante
    simple_figures.create_arc(points_semi_circumference, start=180, extent=270) #Il keyword argument "start" rappresenta il quadrante, in angoli, dalla quale la semi-circonferenza viene posizionata, mentre il keyword argument "extent" rappresenta l'angolo di estensione totale della circonferenza


    simple_figures.pack()
    geometry_window.mainloop()

main()