#Il modulo .loc[], localization, e il modulo .iloc[], index localization, hanno esattamente la stessa funzione, con la differenza che: 
#Il metodo .loc[] prende come positional arguments delle stringhe come coppia coordinate (riga e colonnna), mentre .iloc[], indipendentemente dal nome delle righe e colonne, i numeri associati ad una riga e colonna specifica.

#Il modulo .loc[], ossia localizalition, stampa una specifica frazione di un dataframe.

print("First Print:\n")

import pandas as pd

df = pd.read_csv("dati_vendite.csv", index_col=0) #Con index_col=0 sono stati rimossi gli indici di default poiché gli indici, adesso, sono gli elementi della riga 0.

print(f"Element taken with .loc[]: {df.loc["2024-01-01", "Quantità"]}") #In questo modo stiamo cercando l'elemento all'indice "2024-01-01", e in particolare la cella "Quantità" in quella riga.

print("\nSecond Print:\n")

df = pd.read_csv("dati_vendite.csv")

print(f"Element taken with .iloc[]: {df.iloc[0,2]}") #In questo caso, utilizzando .iloc[] stiamo cercando l'elemento alla riga 0 e colonna 2 