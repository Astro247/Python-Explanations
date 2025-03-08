#Per iterare gli elementi di un dataframe esistono 3 metodi:
#Il primo metodo, '.items', prende una coppia valori da iterare, ovvero il nome delle colonne e gli elementi contenuti in esse:

import pandas as pd

print("First Print:\n")

df = pd.DataFrame({
                   'A': ["a", "b", "c"],
                   'B': ["d", "e", "f"]
                  })

for column_name, column_element in df.items(): #Questo ciclo printa il nome della colonna e successivamente gli elementi in essa contenuti.
    print(f"Column: {column_name}")
    print(column_element)

#Il secondo metodo, '.iterrows', prende anch'esso una coppia di valori da iterare: L'indice della riga e gli elementi di quest'ultima:

print("\nSecond Print:\n")

df = pd.DataFrame({
                   'A': ["a", "b", "c"],
                   'B': ["d", "e", "f"]
                  })

for row_index, row_elements in df.iterrows(): #Questo ciclo printa l'indice della riga e gli elementi contenuti in ogni riga con specificata la loro colonna di riferimento.
    print(f"Row: {row_index}")
    print(row_elements)

#Infine, il terzo metodo, '.itertuples', ha lo stesso funzionamento logico del metodo '.iterrows', con la differenza di essere più veloce poiché non crea, come invece .iterrows fa, una Series per ogni riga e che prende una sola variabile per iterare.
#In quanto prende una sola variabile per eseguire le iterazioni, è possibile specificare anche cosa si vuole iterare con un'annotazione a punto, per esempio: <variabile>.<nome_colonna> accede agli elementi di quella specifica colonna.
#Se si desidera utilizzare questo metodo, utilizzare degli spazi nei nomi delle colonne ritornerà un "errore", o meglio, la colonna non sarà leggibile per il suo nome, ma verrà printato _(indice colonna), dove "_" sta per "colonna"


print("\nThird Print:\n")

df = pd.DataFrame({
                   'A': ["a", "b", "c"],
                   'B': ["d", "e", "f"]
                  })

print("DataFrame without touching anything:\n")

for row in df.itertuples(): #L'iterazione avviene in questo modo: viene printato l'indice della riga, il nome della colonna e l'elemento contenuto in quella colonna nell'indice di quella riga.
    print(row)

print("\nDataFrame with modifications:\n")

for row in df.itertuples(index=True): 
    print(f"Row {row.Index}: {row.A}, {row.B}")

