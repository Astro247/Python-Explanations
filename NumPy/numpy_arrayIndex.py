#L'indicizzazione degli array in Numpy, siccome lavora con delle liste, funziona esattamente come l'indicizzazione delle liste.

import numpy as np

print("First Print:")

list = [1,2,3,4]
arr = np.array([1,2,3,4])

print(f"Second element list: {list[1]}.\nSecond element array: {arr[1]}.")

#Per gli array a più dimensioni, l'indicizzazione segue comunque le stesse regole delle liste annidate in altre liste.
#Negli array non si mettono più parentesi quadre per più dimensioni, i numeri, letti da sinistra a destra, si riferiscono alle liste più esterne (con la lista più esterna di tutte, ossia quella che definisce la dimensione, esclusa, proprio come per le liste)

print("Second Print:")

multiple_list = [[1,2,3], [4,5,6], [7,8,9]]
arr_2D = np.array([[1,2,3], [4,5,6], [7,8,9]])

print("(list) Third element from the second list: ", multiple_list[1][2])
print("(array) Third element from the second list: ", arr_2D[1,2]) 

multiple_list = [
                [[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]
                ]
arr_3D = np.array([
                  [[1,2,3], [4,5,6]],
                  [[7,8,9], [10,11,12]]
                  ])

print("(list) Second element from the third list: ", multiple_list[1][0][1])
print("(array) Second element from the third list: ", arr_3D[1,0,1]) 

#La struttura degli array in NumPy deve seguire una forma precisa, ogni "riga", infatti, deve essere uguale alle precedenti e alle successive in termini di quantità di liste annidate.

print("Third Print:")

try:

    arr_3D = np.array([
                  [[1,2,3], [4,5,6]], #Quantità di liste nella prima riga diversa alla seconda
                  [[7,8,9]]
                  ])
    
except ValueError:
    print("This array does not follow the NumPy structural rules!")

try:

    first_arr_3D = np.array([
                            [[1,2,3]], #Quantità di liste nella prima riga uguale alla seconda
                            [[4,5,6]]
                            ])
    second_arr_3D = np.array([
                              [[1,2,3], [4,5,6]], #Quantità di liste nella prima riga uguale alla seconda
                              [[7,8,9], [10,11,12]]
                              ])
    print("This two arrays follows the NumPy structural rules")

except ValueError:
    print("This two arrays does not follow the NumPy structural rules!")

#Come anche per le liste, l'indicizzazione può avvenire anche con dei numeri negativi, che prendono gli elementi al contrario.

arr_3D = np.array([
                  [[1,2,3], [4,5,6]],
                  [[7,8,9], [10,11,12]]
                  ])

print(f"Second element first list taken normally: {arr_3D[0,0,1]}.\nSecond element first list taken backwards: {arr_3D[-2,-2,-2]}.")

#Prendendo gli elementi al contrario l'indicizzazione normale (ossia quella che prevede che il primo elemento è indice 0 e non 1 e così via) non viene applicata.
#Questo accade perché scrivere: {arr_3D[-1]} equivale a scrivere: {arr_3D[len(arr_3D)-1]}.