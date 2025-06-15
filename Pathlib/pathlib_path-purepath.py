"""
La libreria pathlib consente di gestire e manipolare percorsi di file e cartelle in modo multipiattaforma, 
evitando i problemi legati alle differenze sintattiche tra i sistemi operativi come Windows e Linux.
"""

from pathlib import Path, PurePath

path = Path("disco/directory/file") # La classe 'Path' contiene metodi che modificano il filesystem (quindi di file/cartelle presenti in quel path).

path2 = PurePath("disco/directory/file") # La classe 'PurePath', invece, contiene metodi che si limitano ad interagire/manipolare solo ed esclusivamente con la stringa path, non potendo lavorare con il filesystem (cioè con i contenuti di quella path).

"""
'PosixPath' è il nome attribuito alla sintassi con cui vengono scritte le stringhe path in Linux, mentre per windows
sono chiamate 'WindowsPath'

Sia la classe "Path" che la classe "PurePath", in quanto classi, non sono "path" effettive, ma creano oggetti con una serie di
chiavi-valori che rappresentano quella path, per esempio:

se -- p = Path("file.txt")

p.exists → Ritorna un bool che dice se il file esiste o meno.
p.name → Ritorna il nome del file (punto finale di una path assoluta)
p.parent → Ritorna il nome della directory parent del file (In questo caso "Pathlib")
p.suffix → Restituisce il formato del file, in questo caso '.txt'
"""