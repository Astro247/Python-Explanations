#Per iterare gli elementi di un'array ci sono due metodi che lo permettono, oppure è possibile farlo in maniera più "manuale" con dei cicli for annidati l'un l'altro.

import numpy as np

print("First Print:\n")

arr = np.array([1,2,3,4,5]) #In questo caso l'array è ad una dimensione, pertanto è sufficiente creare un singolo ciclo.


for i in arr:
    print(i, end=" ") #end=" " signnifica che non manda a capo dopo ogni print, poiché di default è impostato come \n alla fine del print, ma crea uno spazio e ristampa sulla stessa riga.

print("\n")
print("Second Print:")

arr = np.array([
               [1,2,3],[4,5,6]  #In questo caso l'array è a due dimensioni, pertanto i cicli più esterni iterano per le dimensioni più esternestesso discorso per gli array a più dimensioni
               ])

for i in arr: #Itera per gli elementi della prima dimensione (che sono 2)

    print(f"\nFirst Dimension: {i}")
    print(f"Element in the first Dimension (second dimension):", end=" ")

    for j in i: #Itera per gli elementi della seconda dimensione (che sono 3)
        print(j, end=" ")

#Esiste anche il metodo "nditer" che sta per "n dimensions iterations", che esegue tanti cicli for annidati quante sono le dimensioni dell'array automaticamente.

print("\n")
print("Third Print:\n")

arr = np.array([
               [1,2,3],[4,5,6] 
               ])

print("Last Dimension Elements:", end=" ")
for i in np.nditer(arr, flags=["buffered"], op_dtypes=['float']): #Il positional argument "arr" specifica l'array a cui ci stiano riferendo, il keyword argument "flags" modifica il comportamento dell'iterazione, in questo caso il valore associato "["buffered"]" è necessario per convertire il tipo di dato durante l'iterazione, infine il keyword argument op_dtypes modifica il tipo di dato durante l'iterazione.

    print(i, end=" ")

print("\n")

print(f"Original Array's Data Type: {arr[0]}, {arr[1]}",) #La modifica effettuata al tipo di dato con il keyword argument "op_dtypes" avviene solo temporaneamente dentro il ciclo

#Infine, il metodo "ndenumerate" ossia "n dimensions enumarate" oltre a iterare per ogni elemento dell'array, salva anche la posizione di quest'ultimo, infatti è necessario passargli due contatori.

print("\n")
print("Fourth Print:\n")

arr = np.array([
               [1,2,3],[4,5,6] 
               ])

print("Position: Element in that position")
for index, i in np.ndenumerate(arr):
    print(f"{index} = {i}")