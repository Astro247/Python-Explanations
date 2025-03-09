#Per sortare un dataframe esistono due metodi:
#1) 'sort_index' come dice il nome sorta il dataframe per gli indici, inoltre si può scegliere se sortare dal più piccolo al più grande con il keyword argument "ascending" (ascendente) impostato a True, oppure non inserire il keyword argument direttamente, oppure impostarlo a False e avere un'ordinamento di indici di tipi discendente (dal più grande al più piccolo)

import pandas as pd

print("First Print:\n")

dict = {"Nome": ["Aurelio", "Marco", "Giacomo", "Beatrice", "Franco"],
        "Età": [25, 32, 20, 50, 19],
        "Residenza": ["Italia", "Germania", "Ungheria", "Francia", "Spagna"],
        "Crimini Commessi": [0, 1, 0, 2, 0]}

df = pd.DataFrame(dict)

print(f"DataFrame with index sorted ascendingly:\n{df.sort_index(ascending=True)}")

print(f"\nDataFrame with index sorted descendingly:\n{df.sort_index(ascending=False)}")

#2) 'sort_values' sorta delle specifiche colonne del dataframe passate come positional argument nel keyword argument "by", inteso come "sorta per questa colonna", anche in questo caso il keyword argument ascending è presente e se si volesse sortare per più colonne è sufficiente inserire come argomenti del keyword argument "by" una lista con i nomi delle colonne.
#Il sort avviene sia numericamente che alfabeticamente

print("\nSecond Print:\n")

dict = {"Nome": ["Aurelio", "Marco", "Giacomo", "Beatrice", "Franco"],
        "Età": [25, 32, 20, 50, 19],
        "Residenza": ["Italia", "Germania", "Ungheria", "Francia", "Spagna"],
        "Crimini Commessi": [0, 1, 0, 2, 0]}

df = pd.DataFrame(dict)

print(f"DataFrame sorted by name:\n{df.sort_values(by="Nome")}")

print(f"\nDataFrame sorted by age:\n{df.sort_values(by="Età")}")