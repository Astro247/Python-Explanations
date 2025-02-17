#Una variabile tuple è una lista con la caratteristica di essere immutabile, inoltre, a differenza delle liste, le tuple si identificano con delle parentesi tonde.

print("Primo Print:")

my_tuple = (1, 2.5, "ciao")
try:
    my_tuple[0] = 2
    print(my_tuple)
except TypeError:
    print("Non è possibile aggiungere valori alle tuple dopo la loro assegnazione, indipendentemente come")

new_tuple = ()
try:
    for counter in range(3):
        new_tuple[counter] = counter
    print(new_tuple)
except TypeError:
    print("Come nel caso precedente, non è possibile in alcun modo aggiungere valori alle tuple dopo la loro assegnazione")

#Le variabili set sono delle liste, identificate con delle graffe, che qualora presentino elementi ripetuti questi ultimi non vengono considerati
#A differenza delle tuple, nelle set è possibile aggiungere valori con la funzione <Nome Set>.add()

print("Secondo Print:")

my_set = {1,2,4,1,1,1,6,3,6,3}
print("La variabile 'my_set' contiene, escludendo le doppie,", len(my_set), "elementi, sono solo questi:", my_set)

my_set.add(0)
print("Dopo l'inserimento di un nuovo valore ecco la nuova set:", my_set)

