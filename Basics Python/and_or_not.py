#L'operatore "and" ritorna due condizioni come "True" solo se entrambe sono vere

controllo = (5==5 and 4<5)
print("Primo bool:", controllo)

controllo = (5!=5 and 4<5)
print("Secondo bool:", controllo)
print("\n")

#L'operatore "or" ritorna due condizioni come "True" solo se almeno una delle due è vera

controllo = (5==5 or 4<2)
print("Primo bool:", controllo)

controllo = (5!=5 or 4<2)
print("Secondo bool:", controllo)
print("\n")

#L'oeratore "not" nega la condizione ad essa posta

var_intero = input("Inserisci un'intero = ")
var_intero = int(var_intero)
controllo = (not var_intero == 5)
print("Ultimo bool:", controllo)