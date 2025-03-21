#I grafici scatter prendono due positional argument, ossia due numeri, o liste della stessa lunghezza contenenti numeri, che rappresentano una coppia coordinate in un grafico bidimensionale

from matplotlib import pyplot as plt
import numpy as np

x_values = np.random.randint(1,21,100) #Genera 10 coordinate x casuali fra 1 a 20
y_values = np.random.randint(1,21,100) #Genera 10 coordinate y casuali fra 1 a 20
colors = np.random.randint(0,10,100) #Genera 10 fasce di colori casuali (0 indica un opacità massima, mentre 9 un'opacità nulla)
sizes = np.random.randint(100,501,100) #Genera 10 valori casuali fra 100 e 400, rappresentanti la grandenzza dei punti.

plt.scatter(x_values, y_values,
            s = sizes, #"s" è il keyword argument alla quale è assegnato un numero, che rende tutti i punti della stessa dimensione, o in questo caso un'array di dimensioni.
            c = colors, #Il keyword argument "c" sta per "colors" e prende una lista di valori, da 0 a 9, rappresentanti dei colori.
            edgecolors="b", #Questo keyword argument aggiunge un contorno, in questo caso di colore blu, ai punti
            linewidths=2, #Quest'altro keyword argument, correlato al precedente, determina lo spessore dell'edgecolor
            cmap = 'Greens', #Il keyword argument "cmap", che sta per "color maps", modifica la natura del keyword argument "c", facendo sì che i valori considerati fra 0 e 9 non siano colori casuali, ma fasce di opacità di un colore specifico, in questo caso verde.
            )

color_bar = plt.colorbar() #Aggiunge una barra accanto al grafico che rende più semplice la leggibilità dei colori.
color_bar.set_label("Intensity") #Cambia il nome della barra.

plt.xlabel("X coordinates")
plt.ylabel("Y coordinates")
plt.title("Random Generated Values")
plt.grid()
plt.show()