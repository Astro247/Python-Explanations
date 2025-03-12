#Ci sono diversi modi per filtrare i dati, con alcune scritture direttamente dal linguaggio di programmazione C, dato che pandas è basato su NumPy che a sua volta è scritto in C.
#Se si volesse selezionare uno specifico elemento, e di conseguenza tutta la sua riga, in una colonna, sintatticamente parlando scrivere 'print(df["a" == "b"])' è errato, poiché ritorna un valore booleano True o False (df[True] oppure df[False]), ma questo non si riferisce a nessuna colonna.
#Di conseguenza è necessario specificare la colonna dalla quale si vuole verificare uno specifico elemento:

import pandas as pd

print("First Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-'],
              'Sick': ['yes', 'no', 'no', 'no', 'yes']
             }

df = pd.DataFrame(class_dict)

try:
    print(df['Students' == 'Kyle']) #Questa riga di codice genera un'errore, poiché stiamo confrontando se la stringa 'Students' è uguale alla stringa 'Kyle', che ritorna "False"

except:
    print(df[df['Students'] == 'Kyle']) #Questa riga di codice è corretta, infatti stiamo chiedendo di printare solo la riga del dataframe dove nella colonna 'Students' è presente la stringa 'Kyle'

#Se volessimo printare delle specifiche colonne e non tutte, è necessario utilizzare il metodo '.loc[]', successivamente utilizzare la virgola come separazione dopo aver scritto la condizione fra parentesi e scrivere una lista con le colonne desiderate.

print("\nSecond Print:\n")

print(df.loc[(df['Students'] == 'Sophie'), ["Students", "Age", "Grade"]])

#Ovviamente, utilizzare l'operatore "!=" risulterà al print di tutto il dataframe, tranne quello specifico elemento.

print("\nThird Print:\n")

print(df[df['Students'] != 'Vincenzo'])

#Il metodo '.str.containts', come dice il nome, è utilizzato per variaboili stringhe nel dataframe, il metodo infatti prende cme positional argument una stringa e, in questo caso, il print viene effettuato a tutte le stringhe del dataframe che contengono almeno parte della stringa scritta.

print("\nFourth Print:\n")

print(df[(df['Students'].str.contains('a')) | (df['Students'].str.contains('A'))]) #Il simbolo '|' sta per 'or', mentre il simbolo '&' sta per 'and', quando si utilizzano questi simboli, tutte le condizioni devo essere isolate da delle parentesi tonde.

#Questo concetto è anche applicato con valori numerici, non solo stringhe.

print("\nFifth Print:\n")

print(df[df['Age'] >= 25])

#Se invece volessi filtrare solo per specifici elementi presenti in una lista, è sufficiente utilizzare il metodo 'isin' che come positional argument prende la lista di riferimento.

print("\nSixth Print:\n") 

list = ['Jane', 'Aiden']

print(df[df['Students'].isin(list)])