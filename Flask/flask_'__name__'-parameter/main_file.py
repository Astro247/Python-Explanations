"""
Dopo aver dichiarato l'istanza 'app', dalla quale è possibile accedere ai metodi della classe Flask, 
le viene passato l'argomento speciale '__name__' che può assumere due valori a seconda del file che viene eseguito:

1) Il file eseguito assegna al '__name__' di quel file il valore di '__main__'.
2) I file non eseguiti, ma importati, assegnano a '__name__' il nome del file importato.
"""

from flask import Flask

app = Flask(__name__) # Viene creata l'istanza 'app'

print(f"[main_file] __name__ = {__name__}") # Se questo codice viene eseguito, allora __name__ del file "main_file" equivale a __main__

if __name__ == "__main__": # Se __name__ (riferendosi sempre al __name__ del file occorrente) equivale a __main__, quindi se è questo il file ad essere stato eseguito, allora entra nell'if
    print("hello world")