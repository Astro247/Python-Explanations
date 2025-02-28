#Esistono diversi metodi per dividere gli array in più array distinti:

#Il metodo .array_split divide l'array per un numero di volte indicato con un positional argument alla funzione.
#Non è importante se il numero di divisioni passato alla funzione come argomento non divide l'array in array con dimensioni differenti oppure se il numero di divisioni è maggiore della lunghezza degli elementi dell'array.

import numpy as np

print("First Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"Splitted array in two parts: {np.array_split(arr, 2)}") #Output: genera due array ad una dimensione, ciascuni con 5 elementi
print(f"Splitted array in five parts: {np.array_split(arr, 5)}") #Output: genera cinque array ad una dimensione cianscuni con 2 elementi
print(f"Splitted array in nine parts: {np.array_split(arr, 9)}\n") #Output: genera nove array ad una dimensione alcuni con 1 elemento ed altri con più elementi

#Lo stesso principio, con il metodo .array_split, viene applicato anche se vengono introdotte più dimensioni:

arr = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

print(f"Splitted array in two parts:\n {np.array_split(arr, 2)}\n") #Output: genera due array a due dimensioni ciascuno con tre elementi dentro
print(f"Splitted array in three parts:\n {np.array_split(arr, 3)}\n") #Output: genera tre array a due dimensioni, alcuni array hanno due elementi nella prima dimensione, altri solo uno
print(f"Splitted array in four parts:\n {np.array_split(arr, 4)}\n") #Output: genera quattro array a due dimensioni, tutti con un solo elemento nella prima dimensione e tre elementi nella seconda

#Il metodo .split, invece, necessita di un numero di divisioni tale da poter dividere l'array in un numero di array più piccoli con uguali dimensioni e numero di elementi fra loro.

print("Second Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"Splitted array in two parts: {np.split(arr, 2)}")

try:

    print(f"Splitted array in two parts: {np.split(arr, 4)}")

except ValueError:
    print("With the '.split' method, the followed code line cannot be executed\n")

#Il keyword argument 'axis' è un valore booleano che determina come l'array viene splittato nelle parti indicate nel positional argument precedente:
#1) Se 'axis=False', come di default, allora non ci saranno cambiamenti alla divisione dell'array.
#2) Se 'axis=True', allora per ogni array splittato vengono presi singolarmente i primi, secondi, terzi eccetera elementi della dimensione più interna.

print("Third Print:\n")

arr = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]) #Per far si che 'axis=True', l'array deve avere più di una dimensione.

print(f"Splitted array in three parts:{np.array_split(arr, 3, axis=True)}")
print(f"Splitted array in two parts:{np.array_split(arr, 2, axis=True)}") #Se 'axis=True', ma il numero di divisioni in array più piccoli è minore del numero di elementi nella dimensione più interna, allora più elementi vengono inseriti in diversi array.
