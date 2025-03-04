#Le serie in Pandas sono le colonne dei DataFrame, ossia degli array ad una dimensione (o semplici liste) che con la funzione .Series vengono trasformati in tabelle a due colonne, la prima con gli indici degli elementi e la seconda con gli elementi stessi.

import pandas as pd

print("First Print:\n")

list = ['a', 'b', 'c', 'd']

serie = pd.Series(list)

print(serie)

#Se volessimo modificare il nome della colonna degli indici è sufficiente utilizzare il keyword argument "index" e passargli i nomi degli indici, che verranno cambiati in ordine numerico.

print("\nSecond Print:\n")

list = ['a', 'b', 'c', 'd']

serie = pd.Series(list, index=['letter_A', 'letter_B', 'letter_C', 'letter_D'])

print(serie)

#In quanto però stiamo definendo dei nuovi nomi degli indici, e come visto nel DataFrame tutte le liste, colonne, devono avere la stessa lunghezza, se i nomi associati agli indici hanno una lunghezza diversa allora darà errore.

print("\nThird Print:\n")

try:
    list = ['a', 'b', 'c', 'd']

    serie = pd.Series(list, index=['letter_A', 'letter_C', 'letter_D'])

    print(serie)

except ValueError:
    print("The indexes's names aren't as many as the list's elements")

#Un dizionario svolge già questo compito in quanto ad ogni elemento è già assegnato un indice.

print("\nFourth Print:\n")

dict = {'letter_A': 'a', 'letter_B': 'b', 'letter_C': 'c', 'letter_D': 'd'}

serie = pd.Series(dict)

print(serie)

#Nel caso del dizionario, utilizzare il keyword argument 'index' significa specificare quale indice si vuole inserire nella serie, dato che gli indici hanno già un nome loro.

print("\nFifth Print:\n")

dict = {'letter_A': 'a', 'letter_B': 'b', 'letter_C': 'c', 'letter_D': 'd'}

serie = pd.Series(dict, index=['letter_A', 'letter_D'])

print(serie)