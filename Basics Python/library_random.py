#Le librerie in python si inseriscono con il comando "import <Nome Libreria>", come per C le librerie si inseriscono con il comando "include"
#La libreria "random" contiene la funzione "randint(a,b)", che prende numeri casuali da "a" a "b", richiamabile con il comando "<Nome Libreria>.<Nome Funzione>"

import random
print("Primo print:")
for num in range(10):
    print("[",num+1,"] = ", random.randint(1,10), sep="")

#Da una libreria si può chiamare una singola funzione con il comando "from <Nome Libreria> import <Nome Funzione>"
#Con il comando "From" non è necessario specificare la "provenienza" della funzione ed il programma è più leggero, ma sarà solo accessibile quella/quelle funzione/i 

from math import sqrt
print("Secondo print")
val = float(input("Inserisci un numero: "))
print("La sua radice quadrata:", round(sqrt((val)),2))