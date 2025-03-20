#Un grafico hist (istrogramma), è un grafico bidimensionale che rappresenta la frequenza con cui una serie di dati sono salvati in un database.
#La frequenza di apparizione dei dati è detta "bins", in altre parole un bin rappresenta, in un'insieme di dati come una lista o un'array, quanto spesso uno specifico dato oppure uno specifico range di dati appaiono.

import numpy as np
from matplotlib import pyplot as plt

random_datas = np.random.randint(1, 101, size=20)
bins = [10,20,30,40,50,60,70,80,90,100] #Asse x

average = 0
for element in random_datas:
    average = average + element
average = average/20

plt.title("Random Values (1-100)")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.xticks(bins) #Non fa sì che nell'asse x  i valori della lista "bins" vengano distribuiti da matplotlib automaticamente, ma vengono inseriti tutti i valori della lista.
plt.hist(random_datas, #Genera l'istogramma con l'array 1D di 20 elementi di valori randomici da 1 a 100
         bins=bins, #Questo keyword argumet può prendere un valore numerico, che rappresenta il numero di barre che verranno generate, può predere la stringa "auto", che attribuisce un numero di barre automaticamente, oppure una lista, dove le barre generate rispetteranno sempre determinati spazi (specificati come elementi della lista).
         edgecolor="black", 
         alpha=0.2)

plt.axvline(average, #Genera una retta verticale nella coordinata "average"
            color="red", 
            linewidth=3)
plt.show()