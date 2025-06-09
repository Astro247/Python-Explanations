# Il parametro "self" equivale esattamente al "this" di JavaScript.
# "self" e' automaticamente assegnato alla variabile contenente la classe.

class VeichleInfo:

    def __init__(self, type, model, color): # La funzione __init__ è il costruttore, serve a creare l'oggetto.
        self.type = type
        self.model = model
        self.color = color

    def isDriving(self): # Le funzioni interne alla classe diverse dal costruttore si chiamano "metodi".
        print("The veichle " + self.model + " is currently in motion")

    def isNotDriving(self):
        print("The veichle " + self.model + " is currently not in motion")