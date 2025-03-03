#Le ufunc, ovvero 'universal functions' sono funzioni che agiscono su più array in maniera completamente personalizzabile:
#Le ufunc non sono necessarie per operazioni aritmetiche di base native in NumPy, ossia che riesce a farle senza questo genere di funzioni.
#Per tutte le operazioni che non riguardano operatori aritmetici di base, come la concatenazione di stringhe, è necessario utilizzare la universal function.

import numpy as np

print("First Print:\n")

def get_sentence(letter_one, letter_two): #Definisce una funzione con due parametri
    return str(letter_one) + " and " + str(letter_two) #Ritorna la somma dei due parametri

arr_one = np.array([["a","b","c"],["d","e","f"]])
arr_two = np.array([["A","B","C"],["D","E","F"]])

final_sentence = np.frompyfunc(get_sentence, 2, 1) #Fa sì che la fuzione 'get_sentence' diventi una funzione universale e il suo "alias" viene dato al nome "final_sentence".
                                                   #La funzione 'final_sentence' prende come positional argument la funzione nella quale avviene l'operazione, quindi 'get_sentence', il numero di parametri che prende e il numero di output che restituisce.
print(f"Upper and lower letters of the two arrays:\n{final_sentence(arr_one, arr_two)}") #I due array vengono passati alla funzione alias come semplici positional arguments.

#Per le operazioni matematiche di base, anche se queste vengono effettuate fra liste, NumPy converte automaticamente quelle liste in array.

print("\nSecond Print:\n")

arr_one = np.array([1,2,3,4,5])
arr_two = np.array([6,7,8,9,10])

arr = np.add(arr_one, arr_two) #La funzione np.add prende come positional argument i due array e somma i loro elementi.

print(f"Sum of the two arrays: {arr}")

arr = np.subtract(arr_one, arr_two) #Stesso discorso della funzione np.add, ma in questo caso sottrae gli elementi.

print(f"Subtraction of the two arrays: {arr}")

arr = np.multiply(arr_one, arr_two) #In questo caso moltiplica gli elementi.

print(f"Product of the two arrays: {arr}")

arr = np.divide(arr_one, arr_two) #In questo caso divide gli elementi

print(f"Division of the two arrays: {arr}")

arr = np.power(arr_one, arr_two) #La funzione np.power effettua eleva gli elementi del primo array con quelli del secondo.

print(f"Power of the two arrays: {arr}")

arr = np.mod(arr_one, arr_two) #Restituisce il resto della divisione dei due array.

print(f"Mod of the two arrays: {arr}")

#Infine, la funzione 'fix' taglia i numeri decimali di un'elemento in un'array.
#La funzione 'around', invece, arrotonda gli elementi dell'array.

print("\nThird Print:\n")

arr = np.array([1.5, 5.3, 2.8])

print(f"Function 'fix': {np.fix(arr)}")
print(f"Function 'around': {np.around(arr)}")


