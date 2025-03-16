#Matplotlib è una libreria utile per creare dei 'plot', ossia dei grafici.
#Per creare un grafico semplice, piano cartesiano bidimensionale, è necessario importare "pyplot", ossia una parte di libreria di matplotlib utile per questo genere di operazioni.

from matplotlib import pyplot as plt
import numpy as np

print("First Print:\n")

x_axis = np.arange(0,21,1) #Crea la lista dell'asse x del grafico, grazie a NumPy, formata da dei numeri da 0 a 20 con un salto di 1 per ogni numero.
y_axis = np.arange(0,42,2) #Crea la liste dell'asse y ma in questo caso i numeri vanno da 0 a 40 con un salto di 2 per ogni numero

plt.xticks(x_axis) #La funzione '.xticks' fa sì che i tick, ossia i salti fra un valore e l'altro, nel grafico non siano posizionati, per motivi di leggibilità, da matplotlib ma vengono posizionati con il numero di salti specificato in precedenza. 
plt.plot(x_axis,y_axis) #La funzione '.plot' crea il grafico bidimensionale, il primo positional argument passato è l'asse delle x, mentre il secondo quello delle y
plt.show() #La funzione '.show()', proprio come per Tkinter, genera un GUI con il grafico creato.

#In quanto array di NumPy, sia x che y devono essere array con l'ultima dimensione uguale in termini di quantità di elementi.


