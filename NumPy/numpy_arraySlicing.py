#Come per le liste, lo slicing permette di selezionare aree specifiche di una lista nell'array.
#Per selezionare un range di caratteri si utilizzano i ":", dove a sinistra viene inserito l'indice di inizio, mentre a destra l'indice di arrivo (l'indice di arrivo è escluso)

import numpy as np

print("First Print:")

list = ["a","b","c","d","e","f","g"]
arr  = np.array(["a","b","c","d","e","f","g"])

print(f"(list) = Letters From 'b' to 'f': {list[1:6]}")
print(f"(array) = Letters From 'b' to 'f': {arr[1:6]}\n") #In quanto array, nel print non vengono posizionate le virgole
print(f"(list) = Letters From startt to end: {list[:]}")
print(f"(array) = Letters From startt to end: {arr[:]}\n") #Inserire solo ":" è una shortcut per definire il range "inizio:fine"
print(f"(list) = Letters From 'b' to 'f' with backward index: {list[-6:-1]}")
print(f"(array) = Letters From 'b' to 'f' with backward index: {arr[-6:-1]}\n") #Anche se gli indici sono negativi, ciò non significa che l'ordine di contaggio degli indici si inverta a sua volta, vengono comunque contati da sinistra verso destra.

#Selezionare un range di elementi in un array multi-dimensionale segue lo stesso procedimento di specificazione della lista desiderata, con la differenza che, al posto di inserire un indice (una volta selezionata una specifica lista) si inserisce un range.

print("Second Print:")

arr2D = np.array([["a","b","c","d"], ["e","f","g","h"]])

print(f"Letters from 'b' to 'd': {arr2D[0, 1:]}") #Gli argomenti inseriti sono: L'indice indicante la lista di riferimento (0 = prima lista) e il range di valori desiderati in quella lista (dall'indice 1 in poi)

arr3D = np.array([
                  [["a","b","c","d"], ["e","f","g","h"]],
                  [["i","l","m","n"], ["o","p","q","r"]]
                 ])

print(f"Letters from 'i' to 'm': {arr3D[1,0,:3]}")