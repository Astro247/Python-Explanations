#In numpy, "random" è una libreria da includere a parte.
#La funzione randint, ossia "random integer", prende come positional argument un intero, così genererà numeri random da 0 a quell'intero, e come keyword argument "size" degli interi, che determinano le dimensioni che avrà l'array generato.
#La funzione rand, a differenza di randint, genera numeri casuali da 0 a 1, pertanto, non necessitando di un positional argument che determini il range di numeri casuali, di default, come argomenti della funzione, vengono considerati i positional argument che determinano la dimensioni dell'array.

import numpy as np
from numpy import random

print("First Print:\n")

randint_arr = random.randint(10, size=(2,4)) #Alla variabile 'randint_arr' viene assegnato un'array a due dimensioni: la prima dimensione con due elementi e la seconda con quattro elementi casuali da 0 a 10
print(f"Array generated with the 'randint' function:\n {randint_arr}")

rand_arr = random.rand(2,5) #Viene assegnato, alla variabile rand_arr, un array di 2 dimensioni: la prima con due elementi e la seconda con cinque elementi casuali fra 0 e 1
print(f"Array generated with the 'rand' function:\n {rand_arr}")

#La funzione choice prende un numero casuale all'interno di un'array.
#E' possibile creare un nuovo array con la funzione choice, riempiendolo con elementi scelti casualmente da un'altro array. Fra gli argomenti della funzione choice c'è anche il keyword argument "size".

print("\nSecond Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10])

choice_array = random.choice(arr, size=(2,3)) #Il primo positional argument è l'array dalla quale deve prendere gli elementi, con il keyword argument size, in questo caso, è stato chiesto di generare un nuovo array a due dimensioni: la prima con 2 elementi e la seconda con 3 elementi scelti a caso fra gli elementi dell'array.

print(f"Random element from the array taken with the choice function: {random.choice(arr)}") #Prende un elemento casuale nel positional argument "arr" (ossia nell'array)
print(f"New random generated array with the choice function:\n {choice_array}")

#Il keyword argument "p", ossia "probability", della funzione choice, funziona in maniera molto simile all'algoritmo di filtraggio degli elementi di un'array.
#Questo keyword argument considera un'array il quale contiene numeri da 0 a 1 che rispetti due condizioni: il numero di elementi fra 0 e 1 deve essere uguale alla lunghezza dell'array considerato dalla funzione choice e la somma di tutti gli elementi deve essere uguale ad 1.
#Questi numeri, da 0 a 1, infatti rappresentano la probabilità in percentuale che l'elemento nello stesso indice della percentuale inserita venga scelto.

print("\nThird Print:\n")

arr = np.array([1,2,3,4,5])
probability = np.array([0.1, 0.2, 0.2, 0.3, 0.2]) #Il numero uno ha il 10% di possibilità di essere scelto, il numero 2 il 20%, il numero 3 il 20%, il numero 4 il 30% e infine il numero 5 il 20% (in totale tutte queste percentuali sommate sono uguali al 100%)

choice_array = random.choice(arr, p=probability, size=(6))

print(f"Random Generated array with the choice function, probability argument selected: {choice_array}")

#La funzione shuffle e la funzione permutation fanno esattamente la stessa cosa, ossia mischiare randomicamente gli elementi di un'array, con la differenza che:
#La funzione shuffle agisce direttamente su uno specifico array, mentre la funzione permutation, essendo che ritorna un nuovo array, deve essere assegnato a qualcosa.

print("\nFourth Print:\n")

arr = np.array([1,2,3,4,5])

random.shuffle(arr)

print(f"Array modified with the 'shuffle' function: {arr}\n") #Ha modificato direttamente l'array.

arr = np.array([1,2,3,4,5])

random.permutation(arr)
print(f"The following array, with the 'permutation' function, is not modified: {arr}") #Non viene modificato poiché l'array "mischiato" non viene salvato da nessuna parte

modified_array = random.permutation(arr) #L'array modificato viene salvato nella variabile 'modified_array'. Il valore di 'arr' non è cambiato di una virgola.
print(f"This time, with the 'permutation' function, the array is modified: {modified_array}")