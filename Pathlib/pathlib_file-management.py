"""
Con la sintassi default di Python è possibile creare un file nella cwd e poterci interagire utilizzando un 'context manager'.

Il 'context manager' consiste nelle keywords "with open('path-relativa/assoluta', 'tipo-di-interazione') as 'nome-di-riferimento'

Esistono diversi modi con cui è possibile interagire con un file:

- "w" = "write" (scriverci/sovrascriverci se già presente del testo)
- "r" = "read" (legge ciò che è presente nel file come stringa)
- "a" = "append" (aggiunge del testo a del testo già presente)
"""

with open("test1.txt", "w") as file: # In questo caso viene creato un file, o sovrascritto se già esiste, chiamato "test.txt" nel cwd in modalità "w", cioè "writer", assegnando al file .txt la variabile 'file'.
    file.write("hello world") # Con il metodo .write è possibile inserire nel file una stringa.

"""
Con la sintassi di pathlib, invece, ci sono diversi passaggi da seguire per poter creare un file e interagirci
"""

from pathlib import Path

p = Path("test2.txt") # Genera un'oggetto che rappresenta la path che porta al file 'test.txt'.
p.touch() # Crea il file nella path indicata, se già esiste allora lo sovrascrive. (opzionale)
p.write_text("hello world") # Scrive all'interno del file.

"""
Il metodo .stat() ti permette di vedere le statistiche di un file data una certa Path.
"""

from datetime import datetime

file_info = p.stat() # Assegna alla variabile 'file_info' le statistiche del file nella path 'p'.

size = file_info.st_size # dimensione del file in bytes.
last_access = file_info.st_atime # data dell'ultimo accesso. (s dal 1 gennaio 1970)
last_mod = file_info.st_mtime # data dell'ultima modifica. (s dal 1 gennaio 1970)

print(datetime.fromtimestamp(last_access)) # Con la libreria 'datetime' è possibile trasferire i secondi dal 1/1/1970 in una data leggibile
print(datetime.fromtimestamp(last_mod))

mb_dim = (size)/(10**(6)) # Conversione da bytes a megabytes
mb_dim = (size)/(10**(9)) # Conversione da bytes a gigabytes