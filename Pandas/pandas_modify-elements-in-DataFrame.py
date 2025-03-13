#Per modificare i singoli elementi di un dataframe, dunque imporre dei cambiamenti al dataframe quando determinate condizioni vengono rispettate il procedimento è molto semplice.
#Una volta scritta la condizione infatti, utilizzando il metodo .loc[] è sufficiente scrivere fra parentesi tonde le singole condizioni e, dopo aver messo una virgola di separazione, scrivere la colonna che deve essere modificata (Inserire le colonne in una lista se si tratta di molteplici colonne) e una volta aver chiuso tutte le parentesi quadre scrivere in cosa si vuole cambiare l'elemento selezionato.


import pandas as pd

dict = {"Nome": ["Aurelio", "Marco", "Giacomo", "Beatrice", "Franco"],
        "Età": [25, 32, 20, 50, 19],
        "Residenza": ["Italia", "Germania", "Ungheria", "Francia", "Spagna"],
        "Crimini Commessi": [0, 1, 0, 2, 0]}

df = pd.DataFrame(dict)

df.loc[(df['Nome'] == 'Giacomo'), 'Nome'] = 'Francesco'
print(f"DataFrame with the name column modififed:\n{df}")

df["Sickness"] = ["no", "no", "no", "no", "no"]

df.loc[(df['Crimini Commessi'] > 0), 'Sickness'] = 'yes'
print(f"DataFrame with the name modififed:\n{df}")