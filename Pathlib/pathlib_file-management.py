"""
Con la sintassi default di Python è possibile creare un file nella cwd e poterci interagire utilizzando un 'context manager'.

Il 'context manager' consiste nelle keywords "with open('path-relativa/assoluta', 'tipo-di-interazione') as 'nome-di-riferimento'

Esistono diversi modi con cui è possibile interagire con un file:

- "w" = "write" (scriverci/sovrascriverci se già presente del testo)
- "r" = "read" (legge ciò che è presente nel file come stringa)
- "a" = "append" (aggiunge del testo a del testo già presente)
"""

with open("test.txt", "w") as file: # In questo caso viene creato un file, o sovrascritto se già esiste, chiamato "test.txt" nel cwd in modalità "w", cioè "writer", assegnando al file .txt la variabile 'file'
    file.write("hello world") # Con il metodo .write è possibile inserire nel file una stringa.

"""
Con la sintassi di pathlib, invece, ci sono diversi passaggi da seguire per poter creare un file e interagirci
"""

from pathlib import Path

p = Path("test.txt") # Genera un'oggetto che rappresenta la path che porta al file 'test.txt'
p.touch() # Crea il file nella path indicata, se già esiste allora lo sovrascrive. (opzionale)
p.write_text("hello world") # Scrive all'interno del file.

