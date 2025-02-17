#Una variabile è globale se non dichiarata all'interno di una funzione, riconosciuta dunque con un valore all'interno di qualsiasi funzione

print("Primo Print:")
var = 5

def funzione():
    if var == 5:
        print("ciao")
    return var

print(funzione())

#Tuttavia all'interno di una funzione non si può modificare il valore della variabile globale con assegnazione poiché in quel caso si creerebbe una variabile locale
#Una variabile è locale a una funzione se dichiarata all'interno di una funzione.

print("Secondo Print:")
var = 5

def funzione(var_loc):
    var_loc = var_loc + 5 
    return var_loc

print(funzione(var))

#Se si desidera alterare il valore della variabile globale all'interno di una funzione allora si utilizza il comando "global <Nome Variabile Globale>"

print("Terzo Print:")
var = 5

def funzione():
    global var
    var = var + 5 
    return var

print(funzione())