#NumPy è una libreria che serve a lavorare con grandi quantità di dati in maniera molto rapida senza rallentare o appesantire il programma.
#La principale caratteristica che rende NumPy una libreria veloce è che lavora con gli array, che a differenza delle liste in python ha 4 differenze principali:
#1) Gli elementi all'interno dell'array sono più semplici per il computer da individuare, non sono sparsi nella memoria come per le liste.
#2) Essendo NumPy implementato in C, è molto veloce.
#3) Per modificare gli elementi nell'array non è necessario eseguire dei cicli come per le liste, ma è sufficiente eseguire funzioni che agiscono immediatamente per tutti o specifici elementi nell'array.
#4) Gli elementi che NumPy salva negli array non includono informazioni extra che le liste salvano per gli elementi che contengono (come tipo di dato, posizione, eccetera.)


#Nel codice sottostante viene dichiarato un'array e una lista, ad entrambi tutti gli elementi che contengono vengono moltiplicati per 2.

import numpy as np

numbers_array = np.array([1,2,3,4,5])
numbers_list = [1,2,3,4,5]

print("First Print:")

for element in range(len(numbers_list)):
    numbers_list[element] = numbers_list[element]*2

print(numbers_list)
print(numbers_array*2)

#Nel codice sottostante invece alla lista e all'array viene aggiunto +5

numbers_array = np.array([1,2,3,4,5])
numbers_list = [1,2,3,4,5]

print("Second Print:")

try:
    print(numbers_list+2) #Aggiungere un + ad un tipo di dato diverso dagli array in numpy significa concatenare una stringa, ma in questo caso ci da errore perché sta provando a concatenare un intero con una lista.

except TypeError:
    for element in range(len(numbers_list)):
        numbers_list[element] = numbers_list[element]+5

print(numbers_list)
print(numbers_array+5)