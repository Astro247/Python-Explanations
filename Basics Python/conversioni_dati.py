#Le variabili possono essere convertite permanentemente o temporaneammente in un tipo diverso di variabile.

var_intero = 1
var_stringa = "1"

#la somma di queste 2 variabili non è fattibile, poiché una è di tipo numerico, mentre l'altra è di tipo "scritto"
#si può cambiare temporaneamente il tipo di una variabile scrivendo il tipo di variabile e fra parentesi inserire il nome della variabile da modificare:

risultato = var_intero + int(var_stringa)
print("La somma delle due variabili è:", risultato)
print("La variabile \"var_stringa\" rimane sempre di tipo", type(var_stringa), "\n")

#in quanto però il cambiamento di variabile non è stato assegnato, la variabile var_stringa rimane comunque una stringa e solo a riga 9 è temporaneamente diventata un'intero

var_stringa_intero = int(var_stringa)
print("Dopo l'assegnazione, alla nuova variabile \"var_stringa_intero\" è stato assegnato il valore della stringa \"var_stringa\" trasformata in intero.\nInfatti il tipo di dato adesso è", type(var_stringa_intero))
