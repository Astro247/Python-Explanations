#Per creare un file csv oppure excel (xlsx) è sufficiente utilizzare il metodo '.to_csv' oppure '.to_excel'

import pandas as pd

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataframe = pd.DataFrame(class_dict)

class_dataframe.to_csv('class_dict.csv', index=False) #Crea un file .csv partendo dal dizionario creato in precedennza, con keyword argument 'index' impostato a False (eliminando così gli indici numerici generati di default)
class_dataframe.to_excel('class_dict.xlsx', index=False) #Stesso discorso, ma in questo caso è un file .xlsx (excel)

#Se volessimo comprimere il file in formato .zip è sufficiente utilizzare la funzione 'dict'

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataframe = pd.DataFrame(class_dict)

compression_options = dict(method="zip", archive_name='class_dict.csv') #Il keyword argument 'method' specifica il tipo di formato nella quale si vuole salvare il file compresso, mentre il keyword argument 'archive_name' specifica il nome del Dataframe salvato all'interno del file compresso
class_dataframe.to_csv('class_dict.zip', index=False, compression=compression_options) #Il positional argument iniziale non è il nome del Dataframe, ma del file compressio, mentre il keyword argument "compression" è assegnato alle impostazioni salvate nella variabile che contiene gli argomenti specificatti nel "dict".

#Per quanto riguarda excel, in quanto quest'ultimo contiene delle pagine, chiamate 'sheet', è possibile cambiargli il nome con il keyword argument: 'sheet_name'

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataframe = pd.DataFrame(class_dict)

class_dataframe.to_excel('class_dict.xlsx', index=False, sheet_name="Class List") 

#Se volessi creare più sheets in excel, è necessario utilizzare una specie ciclo for con una funzione chiamata "ExcelWriter"

class_dict = {
              'Students': ['Kyle', 'Vincenzo', 'Aiden', 'Sophie', 'Jane'],
              'Age': [25, 35, 23, 20, 19],
              'Grade': ['A+', 'B', 'A', 'C', 'C-']
             }

class_dataframe = pd.DataFrame(class_dict)
class_dataframe.to_excel('class_dict.xlsx', index=False, sheet_name="Class List") 

class_students = class_dataframe['Students']
class_age = class_dataframe['Age']
class_grade = class_dataframe['Grade']

with pd.ExcelWriter('class_dict.xlsx') as writer:
    class_students.to_excel(writer, sheet_name='Students')
    class_age.to_excel(writer, sheet_name='Age')
    class_grade.to_excel(writer, sheet_name='Grade')

#Se volessi aggiungere uno sheet nuovo ad un file excel già esistente è sufficiente utilizzare il keyword argument "mode", come argomento della funzione "ExcelWriter" e impostarlo ad "a", che sta per "append".

class_ageAndgrade = class_dataframe[['Age', 'Grade']]

with pd.ExcelWriter('class_dict.xlsx', mode="a") as writer:
    class_ageAndgrade.to_excel(writer, sheet_name="Age + Grade")
