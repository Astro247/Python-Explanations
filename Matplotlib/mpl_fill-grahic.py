#Per generare zone colorate in un plot è sufficiente utilizzare la funzione ".fill_between()" che accetta 3 positional arguments, coordinate x e coordinate y più un numero su cui si deve basare per colorare determinate aree di grafico.

# WHERE: Il keyword argument "where" permette l'inserimento di condizioni, quindi: "colorami solo le parti di grafico dove.."      
# ALPHA: In quanto il colore del grafico potrebbe risultare troppo intenso, è possibile modificarne l'opacità con questo keyword argument.

import numpy as np
from matplotlib import pyplot as plt

y_axis = np.array([1,2,3,4,5,6,7,8,9,10])
x_axis = np.array([10,20,30,40,50,60,70,80,90,100])
break_color_point = 7

plt.xticks(x_axis)
plt.yticks(y_axis)

plt.plot(color="#960008")
plt.fill_between(x_axis, y_axis,
                 break_color_point, #Questo specifico positional argument è un numero che determina in che modo verrà colorato il grafico rosso. In questo caso dato che il numero è 7, tutta la parte alta di grafico in cui y > 7 viene colorata, ma una volta superata la coordinata y = 7, viene colorata la parte bassa di grafico.
                 color="red",
                 alpha=0.2)

plt.plot()
plt.fill_between(x_axis, y_axis,
                 where=(y_axis>3), #Con questo comando stiamo specificando a matplotlib di colorare in blu la parte di grafico in cui y>=3.
                 color="blue",
                 alpha=0.2)

plt.grid()
plt.show()

#Le liste degli assi sono stati trasformati in array di NumPy per il seguente motivo: Se il codice fosse stato eseguito senza gli array, ma con semplici liste, allora a riga 24 avrebbe causato problemi, poiché il comando "lista > intero" ritorna un TypeError (Una lista non è un numero, ma un'insieme di elementi e quindi non può essere comparata ad un intero)
#Con NumPy invece questa cosa cambia, poiché il comando "array > intero" crea un secondo array contenente valori booleani, in quanto in questo caso non è l'array ad essere confrontato con l'intero, ma gli elementi che esso contiene, pertanto questo non genera errori.