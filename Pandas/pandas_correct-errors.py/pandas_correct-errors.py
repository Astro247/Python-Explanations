#Qualche volta in un DataFrame potrebbero esserci degli errori:
#1) L'elemento 'NaN', abbreviazione di "Not a Number",  indica un'elemento di una colonna non definito o mancante.
#Per risolvere questo problema esistono diversi metodi:

import pandas as pd

print("First Print:\n")

df = pd.read_csv("pandas_file_calories.csv")

print(f"Original DataFrame:\n{df}")

dropna_df = df.dropna() #Il metodo .dropna() elimina completamente le righe con un'elemento mancante 'NaN', è assegnabile ad una nuova variabile creando così un copy del dataframe di partenza oppure, con il keyword argument 'inplace=True', si può modificare il dataframe originale.

print(f"\nDataframe without the 'NaN' rows:\n{dropna_df}")

fillna_df = df.fillna('abc') #Il metodo .fillna() invece modifica gli elementi mancanti, NaN, con un positional argument inserito a piacimento.

print(f"\nDataframe with the 'NaN' replaced with 'abc':\n{fillna_df}")

#Per gli errori legati alle date è sufficiente utilizzare il metodo: .to_datetime, questo metodo infatti converte un'intera Series in formato "data e ora".

print("\nSecond Print:\n")

data_df = df.copy() #Per non modificare il dataframe originale, sfruttando il fatto che pandas è strutturato in NumPy, creiamo un copy del datframe originale
data_df.loc[22, 'Date'] = '2020/12/22' #Utilizzando il metodo .loc[], si poteva usare anche il metodo .fillna, modifichiamo il 'NaN' nella colonna "Date" con una data.
data_df['Date'] = pd.to_datetime(data_df['Date'], format="mixed") #Come positional argument al metodo .to_datetime è stata passata la colonna da modificare del dataframe, mentre il keyword argument "format='mixed'" fa sì che il metodo .to_datetime accetti qualsiasi tipo di formato di data, sia con gli apici che senza.

print(f"\nDataframe with the date fixed:\n{data_df}")

#Per sistemare dei valori in una colonna specifica è sufficiente utilizzare un ciclo, oppure si può manualmente riutilizzare il metodo .loc[]

print("\nThird Print:\n")

df_value = df.copy()

for index in df_value.index:
    if df_value.loc[index, "Duration"] > 60:
        df_value.loc[index, "Duration"] = 60

print(f"\nFixed Duration Column:\n{df_value}")

#Infine, per vedere se ci sono elementi duplicati è sufficiente utilizzare il metodo .duplicated()

print("\nFourth Print:\n")

print(df.duplicated()) #L'output stampa per ogni indice un valore booleano: se è False, significa che la riga è unica, se invece è True allora quella riga è ripetuta da qualche altra parte.

print(df.drop_duplicates()) #La funzione .drop_duplicates risolve questo problema eliminando le righe che ritornano un True.