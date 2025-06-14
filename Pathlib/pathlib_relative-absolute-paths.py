"""
Una path è assoluta se comprende un percorso completo, che parte dalla radice del filesystem.
Una path relativa, invece, è un percorso incompleto, non direttamente risalente alla radice del filesystem.
"""

from pathlib import Path

path1 = Path.cwd() # Il metodo .cwd(), Current Working Directory, ritorna una stringa assoluta che porta alla directory nella quale il file è stato eseguito.

path2 = Path(".") # Il simbolo "." si riferisce anch'essa alla directory nella quale è stato eseguito il file, ma a differenza del metodo .cwd() è una path relativa, non risalente quindi alle radici del filesystem.

if path1 == path2: print("First Test: True")
else: print("First Test: False")

if path1.absolute() == path2.absolute(): print("Second Test: True") # Il metodo .absolute() trasforma qualsiasi path in una path assoluta.
else: print("Second Test: False")