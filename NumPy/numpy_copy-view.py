#Il metodo .copy assegna ad una variabile il contenuto di un'altra variabile array. le due variabili rimangono indipendenti fra loro.

import numpy as np

print("First Print:\n")

arr = np.array([1, 2, 3])
arrCopy = arr.copy()

print(f"Main Array Value: {arr}")
print(f"Copied Array Value: {arrCopy}")

arr[0] = 5

print(f"Main Array Value After Changes: {arr}")
print(f"Copied Array Value After Changes: {arrCopy}")

print(f"Main Array's Base: {arr.base}") #Il metodo .base verifica se un'array è indipendente o dipendente da altri array, se dovesse essere una variabile indipendente allora 'arr.base = None', se invece dovesse essere una variabile dipendente da un'altra allora 'arr.base = [valori array]'
print(f"Copied Array's Base: {arrCopy.base}")

#Il metodo .view, a differenza del metodo .copy, assegna ad una variabile il contenuto di un'altra variabile array, restando dipendente da quest'ultima.
#Qualsiasi cambiamento fatto all'array "originale" affligge anche la variabile dipendente e viceversa.

print("\nSecond Print:\n")

arr = np.array([1, 2, 3])
arrView = arr.view()

print(f"Main Array Value: {arr}")
print(f"View Array Value: {arrView}")

arr[0] = 5 #In questo caso, essendo la variabile arrView dipendente dalla variabile arr, entrambi gli array vengono modificati

print(f"Main Array Value After Changes: {arr}")
print(f"View Array Value After Changes: {arrView}")

print(f"Main Array's Base: {arr.base}") 
print(f"View Array's Base: {arrView.base}")
