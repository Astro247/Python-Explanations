"""
Per verificare che una path punti ad una directory esiste il metodo ".is_dir", mentre per verificare che
punti ad un file è sufficiente usare il metodo ".is_file", entrambi i metodi ritornano un bool.

(un disco è considerato come directory)
"""

from pathlib import Path

p = Path("C:/dir/dir/file") # Siccome pathlib rimuove il problema sintattico delle path fra windows e linux, in entrambi in casi è sufficiente utilizzare il simbolo '/' per separare le diverse dir

if p.is_file(): print("This path points to a file.") # Ritorna True se la path punta ad un file
if p.is_dir(): print("This path points to a directory.") #Ritorna True se la path punta ad una dir