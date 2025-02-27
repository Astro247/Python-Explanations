#Il metodo .shape, associato ad uno specifico array, ritorna il numero di elementi presenti nelle diverse dimensioni contenute nell'array.

import numpy as np

print("First Print:\n")

arr = np.array([                    #Questo array contiene 3 dimensioni
               [[1,2,3], [4,5,6]],
               [[7,8,9], [10,11,12]] 
               ])

print(f"Array's element per dimension: {arr.shape}") #L'output è formato da 3 elementi: il numero di elementi nella terza dimensione, il numero di elementi nella seconda e il numero di elementi nella prima (quindi: (2,2,3))

#Il metodo .reshape è una view, pertanto condivide i dati con l'array con cui si sta riferendo (modificandolo dunque modifica anche l'array di partenza), che permette di ricostruire le dimensioni dei un array.

print("\nSecond Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10]) #Questo array ha una dimensione

print(f"Re-modelled Array:\n{arr.reshape(2,5)}") #In questo caso, i positional arguments "2,5" indicano al reshape di modificare l'array "arr" in modo che abbia una prima dimensione con 2 elementi e la seconda dimensione con 5 elementi (Non è importante la quantità di dimensioni inserite, l'importante è che il prodotto fra tutte le dimensioni inserite sia uguale alla lunghezza dell'array di partenza)

#Nel caso in cui fosse sconosciuta parte della lunghezza dell'array di partenza, è possibile utilizzare un "-1" come keyword argument del metodo .reshape per permettere a numpy di calcolare autonomamente il numero corretto da inserire.
#Utilizzare "-1" come positional argument però ha dei limiti: Non è possibile utilizzare più -1 per più dimensioni (numpy si limita a calcolare il numero corretto da inserire, non in quale posizione)

print("\nThird Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10]) #Questo array ha una dimensione

print(f"Re-modelled Array:\n{arr.reshape(2,-1)}\n") #Vogliamo che la seconda dimensione venga calcolata da numpy

arr_two = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

try:
    print(f"Re-modelled Array:\n{arr_two.reshape(2,-1,-1)}") #Numpy sa bene che le dimensioni corrette da inserire al posto dei '-1' sarebbero '3' e '2', ma non saprebbe in quale ordine: Non sa se inserire (2,2,3) oppure (2,3,2)

except ValueError:
    print("Too many unknown dimensions.")

#Infine, per eseguire il "flattening", ossia rendere un'array ad una sola dimensione esistono due modi:
#Il primo modo consiste nel utilizzare il metodo .flatten()
#Il secondo consiste nel passare come unico keyword argument al metodo .reshape() un '-1'

print("\nFourth Print:\n")

arr = np.array([                    
               [[1,2,3], [4,5,6]],
               [[7,8,9], [10,11,12]] 
               ])

arr_two = np.array([                    
                   [[1,2,3], [4,5,6]],
                   [[7,8,9], [10,11,12]] 
                   ])

print(f"Flattened First Array: {arr.flatten()}")
print(f"Flattened Second Array: {arr_two.reshape(-1)}")
