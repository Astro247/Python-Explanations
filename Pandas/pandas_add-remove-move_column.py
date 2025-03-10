#Per aggiungere una colonna in un dataframe esistono diversi metodi:
#1) Passare un nome, che sarà il nome della nuova colonna, al dataframe e assegnarglici gli elementi che occuperanno quella colonna.

import pandas as pd

print("First Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

df["Sickness"] = ["yes", "no", "yes", "no", "no"]

print(df)

#2)Utilizzare il metodo '.insert' che prende tre positional arguments: l'indice della colonna (posizione nel quale la nuova colonna deve essere posizionata, le altre colonne verranno spostate di conseguenza), il nome della colonna e l'elemento che contiene.

print("\nSecond Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

df.insert(1, "Cool", ["yes", "no", "yes", "no", "no"])

print(df)

#Per rimuovere una colonna da un dataframe esistono 3 metodi:
#1) Il metodo '.drop' prende come positional argument il nome della colonna e come keyword argument 'implace', il quale è assegnato a True se vogliamo che la colonna sia rimossa dal dataframe originale, oppure False se vogliamo creare un nuovo dataframe diverso da quello originale dove non è presente la colonna scelta.

print("\nThird Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

df.drop("Age", inplace=True, axis=1) #Il keyword argument axis=1 determina che vogliamo lavorare con le colonne, se fosse stato 0 allora avremmo lavorato con le righe.

print(df)

#2) La funzione 'del' prende come positional argument il nome della funzione e la rimuove completamente.

print("\nFourth Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

del df["Grade"]

print(df)

#3) Il metodo .pop sposta la colonna rimossa in un dataframe a parte assegnato in una nuova variabile.

print("\nFifth Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

removed_column = df.pop("Students")

print(f"New Dataframe:\n{df}")
print(f"Removed Column:\n{removed_column}")

#Per invertire le colonne a proprio piacimento esistono diversi metodi:
#1) Il più semplice è semplicemente quello di printare la lista contenente il nome delle colonne desiderate in un'ordine a piacere.

print("\nSixth Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

print(df[["Age", "Grade", "Students"]])

#2) Il secondo metodo prevede l'utilizzo di loc oppure iloc, con la logica uguale a quella del metodo precedente.

print("\nSeventh Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

#In entrambi i casai il positional argument ":" indica che vogliamo fare uno slicing predendo tutti gli elementi delle colonne
print(f"DataFrame Using '.loc':\n{df.loc[:,["Age", "Grade", "Students"]]}") #In quanto .loc, quest'ultima accetta i nomi delle colonne
print(f"DataFrame Using '.iloc':\n{df.iloc[:,[1,2,0]]}") #La funzione .iloc invece accetta gli indici relativi alle colonne

#3) Infine, il metodo ".to_list()" prende tutte le colonne del dataframe e successivamente con la funzione .reverse è possibile invertirne l'ordine.

print("\nEighth Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

df = pd.DataFrame(class_dict)

columns = df.columns.to_list()
columns.reverse()

print(f"Reversed Columns:\n{df[columns]}")