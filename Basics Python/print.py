#La funzione print ha il compito di stampare cosa gli venga inserito a schermo, ma all'interno di essa non possono essere eseguite assegnazioni

print("questo è un test.")

#E' possibile utilizzare i doppi apici o singoli apici per stampare a schermo una stringa..
#Qualora invece uscissimo dagli apici per immettere una variabile è necessario terminare la stringa con una "," e se si volesse riaprirla allora mettere "," alla fine del nome della variabile

var_intero = 5
print("Il numero", var_intero, "è un'intero")

#Se si volesse isolare un singolo carattere all'interno dei doppi apici, quindi sterilizzarlo da qualsiasi sua funzione, è sufficiente mettere "\" prima di inserire il carattere

print("Il mio nome non è \"Marco\", ma Mario")

#Per andare a capo nella funzione print ci sono due modi: Si inserisce "\n" quando si vuole andare a capo, oppure si scrive un print con tre apici

print("Andare\na\ncapo\n")
print("""così
si va
a
capo""")
