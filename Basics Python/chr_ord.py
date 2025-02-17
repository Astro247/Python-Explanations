#Ogni numero in rappresenta un carattere "char", viceversa ogni carattere rappresenta un numero detto "ordinal" stabiliti dal modello ascii
#Per trasformare un intero in un carattere char si usa la funzione chr(variabile), mentre per trasformare una stringa in un numero si usa la funzione ord(variabile)

var_stringa = input("Inserire un numero = ")
var_intero = int(var_stringa)
print("Il numero", var_intero, "corrisponde al carattere:", chr(var_intero))

var_stringa = input("Inserire un carattere = ")
print("Il carattere", var_stringa, "corrisponde al numero:", ord(var_stringa))