#La funzione ".where" cerca in automatico un elemento specifico in un'array, salvandone l'indice in un'altro array.

import numpy as np

print("First Print:\n")

arr = np.array([1,2,5,2,6,5,8,6,5,5,2,1])

arr_five_index = np.where(arr == 5)

print(f"In this array: {arr}, the number '5' is located in these indexes: {arr_five_index}")

#La funzione "where" esegue automaticamente il seguente codice:

arr = np.array([1,2,5,2,6,5,8,6,5,5,2,1])
list_five_index = []

for index, element in np.ndenumerate(arr): #Itera sia per gli elementi dell'array che per il loro indice.
    if element == 5:
        list_five_index.append(index) #Salva nella l'indice corrispondente all'elemento "5".

arr_five_index = np.array(list_five_index)

print(f"With the 'for' cycle, the result is the same as using the 'where' method:", end=" ")

for element in arr_five_index:
    print(element, end=" ")

#La funzione ".sort", come dice il nome, sorta automaticamente gli elementi presenti nelle singole dimensioni dell'array (se sono stringhe allora in ordine alfabetico)

print("\n")
print("Second Print:\n")

arr = np.array([7,5,2,4,9,1,3,6,8])
letters_arr = np.array(["af", "cia", "ba"])

print(f"Sorted Array: {np.sort(arr)}")
print(f"Sorted Words: {np.sort(letters_arr)}")

arr2D = np.array([[1,7,3],[6,9,1]])

print(f"Sorted Two Dimensions Array: \n{np.sort(arr2D)}")

#Il termine "filtrare un array" non è associato ad una funzione o ad un metodo, ma ad un'algoritmo che confronta gli elementi di un'array con quelli di un'altro array contenente solo valori booleani.

print("\nThird Print:\n")

arr = np.array([1,2,3,4,5,6,7,8,9,10])

filter_list = arr%2==0 #La variabile 'filter_list' diventa automaticamente una lista che itera per ogni elemento dell'array 'arr', se in quell'array trova un elemento pari, allora viene aggiunta alla lista una variabile booleana True, in caso contrario viene aggiunta una variabile booleana False

arr_filtered = arr[filter_list] #Nella variabile 'arr_filtered' vengono messi a confronto gli elementi dell'array 'arr' con i valori booleani salvati nella lista 'filter_list'. Se un'elemento di 'arr' corrisponde ad un 'True' di 'filter_list', allora quest'ultimo viene salvato nell'array 'arr_filtered', se invece l'elemento corrisponde ad un 'False', viene skippato.

print(f"Even Numbers = {arr_filtered}")

#Ciò che avviene nel codice sovrastante è rappresentato con il codice sottostante:

arr = np.array([1,2,3,4,5,6,7,8,9,10])

filter_list = []

for element in arr:
    if element%2==0:
        filter_list.append(True)
    else:
        filter_list.append(False)
    
arr_filtered = arr[filter_list]
print(f"Even Numbers = {arr_filtered}")
    