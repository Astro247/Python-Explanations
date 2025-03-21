#Aggiungere delle date come coordinate di un grafico è relativamente semplice grazie alla funzione ".plot_date".

from datetime import datetime #Necessario per poter inserire le date
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates #Utile per poter formattare le date a piacimento
from numpy import random as rand

x_axis = []
y_axis = rand.randint(1, 11, 5).tolist() #Crea un'array a una dimensione di 5 elementi da 1 a 10 che converte in una lista con il metodo .tolist()

for day in range(10,15):
    x_axis.append(datetime(2020,5,day)) #Crea una lista contenente 5 date che vanno dal 10 al 15

plt.plot_date(x_axis, y_axis, linestyle="solid") #Crea il grafico con le date, la logica è esattamente la stessa del grafico di base "plot", ma in questo caso in uno dei due assi sono resenti delle date. Il keyword argument 'linestyle' è assegnaot a "solid" creando così una linea che collega tutte le coppie coordinate

plt.xticks(x_axis) #Per evitare errori nella formattazione automatica degli assi (generando per esempio due volte la stessa data) inseriamo solo le date inserite nella lista.
plt.gcf().autofmt_xdate() #Ruota le date per conferire maggiore leggibilità del grafico, stesso discorso poteva essere applicato con la funzione: "plt.xticks(rotation=[gradi_sessagesimali])"
formatted_date = mpl_dates.DateFormatter('%d %b %Y') #Assegnamo alla variabile "formatted_date" una specifica formattazione della data: "giorno (%b), mese (%b), anno (%Y)", se avessimo voluto il mese scritto per intero allora basta scrivere la 'b' maiuscola
plt.gca().xaxis.set_major_formatter(formatted_date) #Con la funzione ".gca" assegnamo quella specifica formatttazione della data, come positional argument, all'asse x

plt.title("Graphic With Dates")
plt.grid()
plt.show()