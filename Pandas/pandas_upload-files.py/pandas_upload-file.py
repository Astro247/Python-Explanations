#Per poter visualizzare una tabella da un formato csv, excel (xlsx) oppure json in python come DataFrame si utilizza il metodo .read

import pandas as pd

print("First Print:\n")

csv_dataframe = pd.read_csv('dati_vendite.csv') #Come positional argument della funzione 'read_csv' è necessario passare la directory del file csv o, se è nella stessa cartella del file python, il suo nome.

print(f"DataFrame of a .csv file:\n{csv_dataframe}\n")

#Lo stesso discorso è applicato anche per i file .json e .xlsx

json_dataframe = pd.read_json('csvjson.json') #Per i file .json

print(f"DataFrame of a .json file:\n{csv_dataframe}\n")

excel_dataframe = pd.read_excel('dati_vendite.xlsx') #Per i file .xlsx (excel)

print(f"DataFrame of a .xlsx file:\n{excel_dataframe}\n")

#Se volessi eliminare gli indici di default è sufficiete utilizzare il keyword argument 'index_col' alla quale deve essere assegnato il valore '0'.
#Attenzione! utilizzare il keyword argument 'index_col' e assegnargli il valore 0 significa non avere più degli indici di riferimento, pertanto il metodo .loc[] non potrà più funzionare.

print("\nSecond Print:\n")

excel_dataframe = pd.read_excel('dati_vendite.xlsx', index_col=0)

print(f"DataFrame of a .xlsx file without the indexes:\n{excel_dataframe}\n")

try:
    excel_dataframe = pd.read_excel('dati_vendite.xlsx', index_col=0)

    print(f"DataFrame of a .xlsx file without the indexes:\n{excel_dataframe.loc[[0,3]]}\n")

except KeyError:
    print("The following DataFrame doesn't have any indexes.\n")

#Con gli indici, invece, è possibile utilizzare la funzione .loc[]

excel_dataframe = pd.read_excel('dati_vendite.xlsx')

print(f"DataFrame of a .xlsx file with only the first and fourth rows:\n{excel_dataframe.loc[[0,3]]}\n")




