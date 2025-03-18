#Per personalizzare un grafico, matplotlib offre diversi keyword arguments/positional arguments del metodo '.plot' e metodi aggiuntivi:

#1) MOLTEPLICI GRAFICI: E' possibile creare più grafici uno sopra l'altro, e tutto ciò che basta fare è creare un nuovo plot. Tutti i plot, però, devono avere un numero di elementi dell'asse x e y della stessa lunghezza.
#2) TITOLO: Per aggiungere un titolo al grafico è sufficiente utilizzare il metodo ".title" e passargli come positional argument la stringa rappresentante il titolo del grafico.
#3) NOMI ASSI: Per dare un nome agli assi, è sufficiente utilizzare il metodo ".xlabel" se si vuole modificare il nome dell'asse x, mentre per quello delle y il metodo è ".ylabel", e come positional argument passargli la stringa che comparirà nel grafico su quell'asse.
#4) LEGENDA: Creare una legenda è molto utile se si utilizzano più grafici sovrascritti. Per crearla è sufficiente utilizzare il metodo ".legend()" e successivamente inserire come keyword argument 'label' del plot di riferimento il nome del grafico.
#5) GRID: Aggiungere una griglia permette una leggibilità del grafico più semplice, per aggiungerla basta utilizzare il metodo ".grid()"
#6) COLORI: Per cambiare il colore delle linee generate nei plot è sufficiente al keyword argument "color" del plot desiderato un colore o un valore hex.
#7) MARCATORI: I marcatori rendono ancora più semplice la leggibilità di un plot, quello che fanno è semplicemente marcare con un "." le zone del grafico in cui la linea generata tocca il grid. per utilizzarli è sufficiente passare al keyword argument "marker" del plot desiderato uno stile del mark ("o","." ecc..)
#8) STILE LINEA: Per cambiare lo stile di una linea è sufficiente utilizzare il keyword argument "linewidth" e passargli un numero che determina lo spessore della linea, inoltre il keyword argument "linestyle" modifica il tipo di linea, se tratteggiata o meno, e ad esso vanno passate stringhe specifiche, ossia dei tipi specifici di linee.

from matplotlib import pyplot as plt
import numpy as np

x_axis = np.arange(0,21,1)
y_axis = np.arange(0,42,2)
second_y_axis = np.arange(0,63,3)

plt.plot(x_axis,y_axis, label="Graphic A", color="red", linewidth=2, linestyle="--")
plt.plot(x_axis,second_y_axis, label="Graphic B", color="blue", marker=".") #Questo grafico verrà posizionato sotto il precedente

plt.title("Test Graphic") #Aggiunge un titolo al grafico
plt.xlabel("x values") #Aggiunge un nome all'asse x
plt.ylabel("y values") #Aggiunge un nome all'asse y
plt.legend()

plt.grid()

plt.show()