#Per raggruppare determinati tipi di dati in un dataframe esiste un metodo chiamato: 'groupby' che permette di raggruppare diversi elementi del dataframe che condividono qualcosa fra loro.

import pandas as pd

print("First Print:\n")

dict = {"Name": ['Carlo', 'Kyle', 'Jack', 'Julia', 'Jacob', 'Stelio'],
        "Age": [21, 53, 15, 25, 11, 17],
        "Type": ['a', 'b', 'a', 'a', 'b', 'a'],
        "Force": [53, 69, 9, 30, 46, 97]}

df = pd.DataFrame(dict)

group = df.groupby('Type')

print(group.groups) #L'output è un dizionario nel quale come indici vengono printati i singoli elementi diversi fra loro (quindi in questo caso 'a' e 'b') e come elementi degli indici delle liste contenenti le posizioni in cui quell'indice è presente nella colonna 'Type'.

#Lo stesso discorso si applica anche con più colonne selezionate:

print("\nSecond Print:\n")

group = df.groupby(['Type', 'Age'])

print(group.groups) #In questo caso viene printato un dizionario che come indici prende delle liste con una coppia di elementi (un'elemento dalla colonna 'Type' e un'elemento dalla colonna 'Age') e come elemento di quell'indice un'ulteriore lista con all'interno la posizione in cui i due elementi presenti nella lista indice combaciano.

#Come appena visto, il metodo 'groupby' itera per due elementi: l'indice scelto e gli elementi presenti in quegli specifici indici (infatti crea una dizionario come output).

print("\nThird Print:\n")

group = df.groupby('Type')

for (element_type,element_position) in group:
    print(f"Element's name: {element_type}\n Element's group: {element_position}\n") #L'output sono due dataframe diversi dove per ogni dataframe ci sono solo gli elementi di 'a' e 'b' separati.

#Il metodo .mean fa la media di tutti gli elementi numerici di un particolare tipo di elemento.

print("\nFourth Print:\n")

group = df.groupby(['Type']).mean(numeric_only=True)[['Age', 'Force']] #Il keyword argument 'numeric_only=True' fa sì che le colonne la cui media viene calcolata siano solo numeriche.

print(group) #L'output prevede un dataframe con la colonna 'Type', con i singoli elementi 'a' e 'b' seguita dalla media di tutti gli elementi della colonna 'Force' e 'Age' che hanno anche nella stessa riga il tipo 'a' o 'b'

#I valori possono essere anche sortati per una specifica colonna con il metodo '.sort_values'

print("\Fifth Print:\n")

group = df.groupby(['Type']).mean(numeric_only=True)[['Age', 'Force']].sort_values(by='Force')

print(group) #Gli elementi della colonna 'Force' vengono sortati dal più piccolo al più grande, modificabile con il keyword argument 'ascending'