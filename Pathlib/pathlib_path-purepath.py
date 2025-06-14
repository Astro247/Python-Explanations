"""
La libreria pathlib consente di gestire e manipolare percorsi di file e cartelle in modo multipiattaforma, 
evitando i problemi legati alle differenze sintattiche tra i sistemi operativi come Windows e Linux.
"""

from pathlib import Path, PurePath

path = Path("disco/directory/file") # La classe 'Path' permette l'accesso ad una path locale e alla modifica del filesystem (quindi di file/cartelle presenti in quel path).

path2 = PurePath("disco/directory/file") # La classe 'PurePath', invece, si limita ad interagire/manipolare solo ed esclusivamente con la stringa path, non potendo lavorare con il filesystem (cioè con i contenuti di quella path).

"""
'PosixPath' è il nome attribuito alla sintassi con cui vengono scritte le stringhe path in Linux, mentre per windows
sono chiamate 'WindowsPath'
"""