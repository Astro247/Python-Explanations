#Esistono diversi modi dai metodi al semplice slicing per leggere delle specifiche frazioni di dati in un dataframe.
#In primo luogo esiste lo slicing, che applica lo stesso ragionamento utilizzato per le stringhe.

import pandas as pd

print("First Print:\n")

df = pd.read_excel("dati_vendite.xlsx")

print(df[2:4]) #Prende dalla riga 2 alla riga 3

#Il primo metodo per leggere specifici dati in un dataframe è utilizzare la funzione .head, che prende come positional argument un numero che corrisponde agli elementi da leggere partendo dal primo e muovendosi verso il basso.

print("\nSecond Print:\n")

df = pd.read_excel("dati_vendite.xlsx")

print(df.head(3)) #Prende le prime tre righe

#In maniera analoga il metodo .tail ha lo stesso funzionamento del metodo .head con la differenza che il positional argument passatogli è un numero che corrisponde agli elementi da leggere partendo dall'ultimo e muovendosi verso l'alto.

print("\nThird Print:\n")

df = pd.read_excel("dati_vendite.xlsx")

print(df.tail(3)) #Prende le ultime tre righe

#Lo stesso discorso si applica anche con le colonne, se volessi prendere delle colonne specifiche è sufficiente inserire il nome delle colonne che voglio considerare in una lista.

print("\nFourth Print:\n")

df = pd.read_excel("dati_vendite.xlsx")

print(df[["Prodotto", "Data"]]) #Printa solo le colonne "prodotto" e "data"

#I metodi .head, .tail e lo slicing si applicano anche per le colonne:

print("\nFifth Print:\n")

df = pd.read_excel("dati_vendite.xlsx")

print(df[["Prodotto", "Data"]].head(3)) #Prende le prime tre righe delle colonne "prodotto" e "data"