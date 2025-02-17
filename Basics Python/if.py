#L'istruzione "if" controlla una riga di codice, qualora quest'ultima dovesse ritornare un valore booleano True, allora quella parte di codice dentro l'if viene eseguito

age = 18
var_bool = (age>=18)
if age>=18:
    print("Primo Print: in quanto l'età è maggiore o uguale a 18, il valore booleano è", var_bool)

#L'istruzione else esegue il codice che la contiene qualora il controllo effettuato dall'if ritorna un valore booleano False

age = 13
var_bool = (age>=18)
if age>=18:
    print("Primo Print: in quanto l'età è maggiore o uguale a 18, il valore booleano è", var_bool)
else:
    print("Secondo Print: in quanto l'età è minore di 18, il valore booleano è", var_bool)

#L'istruzione elif, ossia "else-if", è un'ulteriore controllo di una nuova riga di codice qualora l'if di partenza ritorna un valore booleano "parzialmente" False

age = 18
drugs_taken = True
var_bool = (age>=18)
if age>=18 and drugs_taken==False:
    print("Primo Print: in quanto l'età è maggiore o uguale a 18, il valore booleano è", var_bool)
elif age>=18 and drugs_taken==True:
    print("Terzo Print: Il ragazzo maggiorenne è sotto effetti di droghe")
else:
    print("Secondo Print: in quanto l'età è minore di 18, il valore booleano è", var_bool)