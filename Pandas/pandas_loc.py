#La funzione .loc[], ossia localization, è utilizzata nei DataFrame, quindi nei dizionari fatti a tabella, quest'ultima prende come positional argument una lista contenente i nomi associati agli indici alla quale deve fare riferimento.
#In altre parole nella lista sono inseriti i nomi degli indici che verranno inseriti in quel dataframe, gli altri verranno esclusi.

import pandas as pd

print("First Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataframe = pd.DataFrame(class_dict)

print(f"Whole list:\n{class_dataframe}\n")

print(f"Vincenzo's Info:\n{class_dataframe.loc[[1]]}\n")

print(f"Vincenzo and Sophie's Info:\n{class_dataframe.loc[[1,3]]}")

#Modificando i nomi degli indici con il keyword argument "index" cambiano anche i nomi da assegnare come positional arguments alla funzione .loc[]

print("\nSecond Print:\n")

class_dataframe = pd.DataFrame(class_dict, index=["Num1", "Num2", "Num3", "Num4", "Num5"])

print(f"Whole list:\n{class_dataframe}\n")

print(f"Kyle and Jane's Info:\n{class_dataframe.loc[["Num1","Num5"]]}")

#Il motivo per cui è necessario utilizzare il metodo .loc[] piuttosto che selezionare direttamente l'indice fra parentesi quadre come si farebbe per una lista, in questo modo: 'class_dataframe[0]' è molto semplice:
#Utilizzando il metodo .loc[], come positional argument vengono ricercare le righe del dataframe, che di default sono indicizzate con dei numeri da 0 a n-1.
#Non utilizzare il metodo .loc[] significa assegnare come positional argument fra le parentesi quadre, class_dataframe[], il nome della colonna, che non è di default indicizzata a qualcosa.
#Pertanto, se python non dovesse trovare una colonna con il nome scritto come positional argument, ritorna un keyerror.