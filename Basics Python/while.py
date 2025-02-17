#Il ciclo while ripete il codice che lo contiene fino a quando la riga di codice che sta verificando non riporta un valore booleano False.

counter = 0
print("Primo print:")
while counter<=5:
    print(counter)
    counter += 1
print("\n")

#Qualora il ciclo si volesse interrompere quando un'altra condizione ritorna una variabile booleana True si utilizza il comando break

counter = 0
print("Secondo print:")
while counter<=5:
    if counter == 3:
        print("Fine dei numeri")
        break
    print(counter)
    counter += 1
print("\n")

#Se invece si volesse saltare il ciclo se un'altra condizione ritorna una variabile booleana True si utilizza il comando continue

counter = 0
print("Terzo print:")
while counter<=5:
    if counter == 3:
        print("Numero Saltato")
        counter += 1
        continue   
    print(counter)
    counter += 1
print("\n")


