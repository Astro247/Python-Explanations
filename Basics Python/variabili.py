#alle variabili può essere assegnato un valore tramite un processo detto "assegnazione", ossia con l'uguale, ed è possibile osservarne il tipo con l'operatore "type"

# variabile int = numero intero

var_intera = 1

#variabile float = numero con numeri decimali (anche .0)

var_float = 1.1

#variabile str = numeri cammuffati in lettere

var_stringa = "a"

print(var_intera, "è una variabile di tipo", type(var_intera))
print(var_float, "è una variabile di tipo", type(var_float))
print(var_stringa, "è una variabile di tipo", type(var_stringa))

#le variabili possono essere utilizzate esattamente come numeri dopo essere state assegnate

risultato = var_intera + var_float
print("la somma fra", var_intera, "e", var_float, "è", risultato)

risultato = var_stringa + var_stringa + " " + var_stringa
print("sommando fra loro variabili", type(var_stringa), "si possono ottenere questo genere di cose:", risultato)