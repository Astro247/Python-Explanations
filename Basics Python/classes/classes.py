# Per non rendere il file contenente il codice principale intasato è preferibile creare una classe in
# Un'altro file per poi importare quella classe nel file principale.

from VeichleClass import VeichleInfo

myVeichle = VeichleInfo("car", "ferrari", "blue") # Gli argomenti vengono passati al costruttore che rende "myVeichle" un'oggetto.
print(myVeichle.type) # Printa il valore associato alla key "type".
myVeichle.isNotDriving() # Viene richiamata la funzione interna alla classe, ossia il metodo.
myVeichle.isDriving()