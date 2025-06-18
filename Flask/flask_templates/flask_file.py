from flask import Flask, render_template # Importando "render_template" è possibile far sì che una funzione ritorni direttamente un file .html, invece di inserire direttamente il codice sottoforma di stringa.
from flask_dict import posts_info

app = Flask(__name__)

@app.route('/')
def headToHomepage():
    return render_template('flask_home.html', posts=posts_info, title="Home") # I keyword arguments sono variabili utilizzate nella sintassi di Jinja nel documento html.

@app.route('/about')
def headToAboutpage():
    return render_template('flask_about.html', title="About")

if __name__ == "__main__": app.run(debug=True)

# NB: Le diverse pagine html solitamente sono inserite in una cartella "templates", mentre i file che non subiscono modifiche dinamiche, come css o js, solitamente sono inseriti in un file "static"