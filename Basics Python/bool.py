#Sono dette variabili booleane quelle variabili che assumono solo i valori "True", ossia 1, e "False", ossia 0

var_insert = input("Inserisci un numero uguale a 5: ")
var_insert = int(var_insert)
if 5==var_insert:
    var_bool = True
    print("Hai inserito un numero uguale a 5, pertanto la booleana ritorna:", var_bool)
else:
    var_bool = False
    print("Hai inserito un numero diverso da 5, pertanto la booleana ritorna:", var_bool)