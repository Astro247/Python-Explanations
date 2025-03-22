#Per mostrare più grafici contemporaneamente, lavorando quindi con i subplot (ossia "plot secondari"), è possibile:
#1) Farlo creando più finestre separate, le finestre si chiamano "figure". 
#2) Utilizzando più grafici nella stessa finestra, i grafici si chiamano "axis".

from matplotlib import pyplot as plt
from numpy import random as rand

first_fig, (first_ax1, first_ax2) = plt.subplots(nrows=2, ncols=1) #Genera il primo subplot utilizzabile, composto da una figure (finestra) e due grafici, infatti il frame della la figure è disposta, come specificato dai keyword arguments della funzione ".subplots", da due righe e una colonna (quindi i due grafici saranno su due righe diverse, ma sulla stessa colonna)
second_fig, second_ax = plt.subplots() #Genera un secondo subplot utilizzabile, ma in questo caso è una figure diversa, quindi una seconda finestra.

x_axis_first_graph, x_axis_first_graph2, x_axis_second_graph = [rand.randint(1, 11, 5).tolist() for _ in range(3)] #Utilizzando la list comprehension generiamo 3 array a una dimensione contenenti 5 valori interi randomici, grazie a NumPy, che variano da 1 a 10, convertendo poi gli array in liste con la funzione ".tolist()" (il ciclo for alla fine prende una variabile "_" temporanea da utilizzare per riempire gli array ed è un ciclo da ripetere per un range uguale al numero di variabili da riempire, in questo caso infatti il range è impostato a 3 perché ci sono 3 variabili da riempire).
y_axis = rand.randint(1, 11, 5).tolist() #Genera un array a una dimensione con 5 elementi casuali, asse y utilizzato in ogni grafico, che variano fra 1 e 10, convertito poi in una lista.

first_ax1.plot(x_axis_first_graph, y_axis, marker="o") #Stiamo creando un plot riferendoci alla prima riga della prima figure
first_ax1.set_title("First Graphic") #Quando si utilizza un nome di una riga, invece che l'abbreviazione ".plt", alcuni comandi necessitano il ".set_" prima, come per il comando "title"
first_ax1.grid()

first_ax2.plot(x_axis_first_graph2, y_axis, marker="o") #Qui invece stiamo creando un secondo plot sempre nella prima figure ma nella seconda riga
first_ax2.set_title("Second Graphic")
first_ax2.grid()

second_ax.plot(x_axis_second_graph, y_axis, marker="o") #Infine, in questo caso stiamo creando un plot su un'altra figure
second_ax.set_title("Second Figure's Graphic")
second_ax.grid()

plt.show()