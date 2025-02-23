#Gli array possono avere più dimensioni, le dimensioni di un'array dipendono dalla quantità di liste annidate che contengono.

import numpy as np

print("First Print:")

zeroDimension_Array = np.array(1) #Questo array non contiene liste, pertanto ha zero dimensioni
print(f"{zeroDimension_Array}. dimensions = {zeroDimension_Array.ndim}") #Il metodo .ndim ritorna il numero di dimensioni di un'array

oneDimension_Array = np.array([1]) #Questo array contiene una lista, pertanto ha una dimensione
print(f"{oneDimension_Array}. dimensions = {oneDimension_Array.ndim}")

twoDimension_Array = np.array([[1]]) #Questo array contiene una lista annidata in un'altra lista, pertanto ha due dimensioni
print(f"{twoDimension_Array}. dimensions = {twoDimension_Array.ndim}")

threeDimension_Array = np.array([[[1]]]) #Questo array contiene una lista annidata in un'altra lista annidata in un'altra lista, pertanto ha due dimensioni
print(f"{threeDimension_Array}. dimensions = {threeDimension_Array.ndim}")

#Un'altro modo più rapido per definire le dimensioni di un'array è assegnando alla funzione "ndmin" il numero di dimensioni desiderate.

print("\nSecond Print:")

fiveDimension_Array = np.array([1,2,3], ndmin=5)
print(f"{fiveDimension_Array}. dimensions = {fiveDimension_Array.ndim}")

#Il metodo .arange prende tre keyword arguments: il numero da cui l'array inizia, il numero dove l'array finisce e il numero che definisce i salti fra un numero e l'altro.

print("\nThird Print:")
arange_array = np.arange(5,55,5) #Questo array inizia dal numero 5, arriva al numero 50 e ad ogni elemento c'è un salto di 5 (Il numero finale viene escluso)
print(arange_array)

#Il metodo .zeros è un metodo che prende diversi keyword arguments inseriti in una tuple, i quali definiscono il numero di liste annidate. L'ultimo numero inserito definisce il numero di elementi "0" dentro le liste.
#Lo stesso identico ragionamento si applica anche per il metodo .ones

print("\nFourth Print:")

zeros_array = np.zeros((3,2,4)) #Questo array contiene 3 liste più esterne, dove ogni lista contiene 2 liste più interne ed ognuna delle 2 liste contiene 4 zeri
print(f"Dimension = {zeros_array.ndim}") #Il primo parametro è un 3, pertanto la dimensione dell'array è 3 (ci sono in totale 3 liste annidate tra loro)
print(zeros_array)