#Il ciclo for non è altro che un ciclo while il cui codice modifica il valore di una variabile fino a quando quest'ultima non ritorna una variabile booleana False.

num = 0
print("Ciclo while:")
while num<6:
    print(num)
    num+=1

num = 0

print("Ciclo for:")
for num in range(6):
    print(num)

#La funzione "range(a,b,c)" considera un range di numeri che iniziano da "a", finiscono a "b" e avanzano/decrescono di "c"
#Per esempio: scrivere "range(5)" è equivalente a scrivere "range(0,5,1)", dunque la funzione inizia da 0, finisce a 5 e incrementa ogni volta di 1

print("Codice finale")
num = 0
for num in range(0,11,2):
    print(num)