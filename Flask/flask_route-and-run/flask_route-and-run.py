"""
Per poter eseguire una funzione una volta che si accede ad un determinato link, è necessario utilizzare
il metodo '@istanza.route()', dove come positional argument è inserita la parte finale di un URL (ossia la parte di URL dopo l'host)
"""

from flask import Flask

app = Flask(__name__) # Viene dichiarata l'istanza 'app'

@app.route('/') # Esegue la funzione 'show_homepage' se il link che termina con '/', solitamente la homepage
def show_homepage():
    return "This is the homepage!"

@app.route('/about') # Esegue la funzione 'show_about' se il link che termina con '/about'
def show_about():
    return "This is the about page!"

if __name__ == "__main__": 
    app.run(debug=True) # Il file viene runnato in una pagina web, con il keyword argument "debug" impostato a True, se dovessero esserci errori questi vengono mostrati direttamente nel sito.