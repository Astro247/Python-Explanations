#Pandas, con l'aiuto di NumPy, è una libreria che si basa sulla modifica e visualizzazione chiara di più tipi di dati.
#La funzione .DataFrame trasforma i dati di un dizionario in una tabella, prendendo l'indice della tabella come "titolo" di una tabella verticale contenente gli elementi della lista alla quale quello specifico indice fa riferimento.
#Tutte le liste utilizzate nel dizionario, durante l'esecuzione della funzione .DataFrame, vengono trasformate in array di NumPy.
#A meno che non si voglia lavorare direttamente con NumPy, non è necessario importarlo quando si lavora solo con Pandas, poiché Pandas è costruito su NumPy, in altre parole NumPy viene importato internamente automaticamente durante l'importazione di Pandas.

import pandas as pd

print("First Print:\n")

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataFrame = pd.DataFrame(class_dict) #Dopo aver dichiarato la funzione .DataFrame è necessario passargli come positional argument il dizionario dal quale deve creare la tabella
              
print(class_dataFrame)

#Tutte le liste, nel dizionario, devono avere la stessa lunghezza, altrimenti la tabella avrà punti in cui un indice non indicizzerà niente.

print("\nSecond Print:\n")

try:
    class_dict = {
                  'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
                  'Age': [25, 35, 23, 19], #Rimossa un età
                  'Grade': ['A+', 'B', 'A', 'C', 'C-']
                 }
    
    class_dataFrame = pd.DataFrame(class_dict)        
    print(class_dataFrame)

except ValueError:
    print("The arrays aren't the same lenght.")