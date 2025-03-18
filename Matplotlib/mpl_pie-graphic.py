#Per mostrare a schermo un grafico a torta è sufficiente utilizzare la funzione ".pie", modificabile attraverso diversi keyword arguments.

#1) LABELS: Il keyword argument 'labels' è assegnato ad una lista contenente i nomi di riferimento alle fette di torta nel grafico
#2) WEDGE-PROPS: Questo keyword argumet è un dizionario con diverse funzionalità, fra cui quella di poter aggiungere una linea di contorno alle fette e all'intero cerchio, con indice "edgecolor" ed elemento il colore della linea di contorno.
#3) COLORS: 'colors' è un keyword argument assegnato ad una lista contenente dei colori, o valori hex, dove l'indice del colore nella lista è uguale all'indice dell'elemento nella lista passata come positional argument iniziale.
#4) START-ANGLE: E' un keyword argument che, essendo il grafico a torta un cerchio, prende come valore un numero rappresentante l'angolo di rotazione del cerchio.
#5) EXPLODE: Qualora si volesse che una fetta sia staccata dal grafico, è possibile farlo con il keyword argument 'explode' che prende una lista di elementi numerici, la cui lunghezza e indici devono essere uguali alla lista del positional argument di partenza, dove l'elemento '0' significa che la fetta non è staccata, se invece è '>0' allora la fetta è staccata dal cerchio.
#6) PERCENTUALE: Per aggiungere una percentuale all'interno delle singole fette è sufficiente utilizzare il keyword argument: 'autopct',  che sta per "auto percentuale", e passargli questa stringa: "%1.1f%%"

from matplotlib import pyplot as plt

slices = [50, 23.74, 74.1, 15.9] #Valori da inserire (non sono le percentuali e la somma dei valori non deve essere uguale a 100, matplotlib calcola automaticamente la somma degli elementi della lista e calcola la percentuale in base a quella somma)
chosen_labels = ["A", "B", "C", "D"]
chosen_colors = ['#699ff5', "#9369f5", "#c25d8f", "#7ec26d"]
chosen_explode = [0, 0, 0.05, 0] #La fetta '74.1' è staccata dal cerchio.

plt.pie(slices, 
        labels=chosen_labels,
        wedgeprops={"edgecolor": "black"},
        colors=chosen_colors, 
        explode=chosen_explode, 
        startangle=15, #Il cerchio è ruotato di 15°
        autopct="%1.1f%%")
plt.title("Text Pie Graphic")
plt.show()