#Le variabili dizionari sono delle liste, identificate come: {<Nome Indice>: <Nome Elemento>}, alle quali è assegnato, per ogni valore contenuto al loro interno, uno specifico indice personalizzato.

print("Primo Print:")

my_dict = {"name": "Marco", "age": 25, "height": 1.78}
print(my_dict)
print("Il mio nome è", my_dict["name"], "ed ho", my_dict["age"], "anni")

prev_name = my_dict["name"]
my_dict["name"] = "Massimo"
print("Mi chiamo", my_dict["name"], "ed ho rubato il nome a", prev_name)

#Gli operatori "in" e "not in", nelle variabili dizionari, sono utili per verificare che un determinato indice sia presente o meno ritornando un valore booleano.

print("Secondo Print:")

food_in_fridge = {"Meat": ["Bacon", "Sausage"], "Vegetables": ["Lattuce", "Tomato"], "Fruits": ["Apple", "Orange"]}
if "Meat" in food_in_fridge or "Beer" in food_in_fridge:
    print("E' rimasta della carne")
else:
    print("Non c'è più carne")

if "Knives" not in food_in_fridge:
    print("I coltelli non sono nel frigorifero")
else:
    print("Hai trovato un coltello nel frigorifero")
    
#Per cancellare una coppia chiave-elemento da un dizionario esiste l'istruzione: del <Nome Dizionario>[<Nome Chiave>]

print("Terzo Print:")

print("In frigo ci sono queste cose:", food_in_fridge)
del food_in_fridge["Meat"]
print("Tolta la carne rimangono questi elementi:", food_in_fridge)

#La funzione: <Nome Dizionario>.keys() ritorna solo le chiavi delle coppie chiave-elemento, la funzione: <Nome Dizionario>.values solo gli elementi, mentre la funzione: <Nome Dizionario>.items ritorna sia le chiavi che gli elementi come tuple

print("Quarto Print:")

my_dict = {"uno": 1, "due": 2, "tre": 3}
print("Ecco le chiavi del dizionario:", list(my_dict.keys()))
print("Ecco gli elementi del dizionario:", list(my_dict.values()))
print("Ecco le chiavi e gli elementi del dizionario:", list(my_dict.items()))

#Per svolgere una funzione qualora all'interno del dizionario non sia presente una chiave è presente la funzione: <Nome Dizionario>.get(Nome Chiave, Funzione)

print("Quinto Print:")
print("Cibo in frigo:", list(food_in_fridge))

if "beer" not in food_in_fridge:
    print("Non c'è alcuna birra.")
else:
    print("C'è della birra (parte 1)")

try:
    print(food_in_fridge["beer"])
except KeyError:
    print("Non c'è alcuna birra (parte 2)")

food_in_fridge.get("birra", print("Non c'è più birra (parte 3)"))

#Le tre righe di codice sovrastanti fanno esattamente lo stesso controllo

#Per aggiungere una coppia chiave-elemento, qualora non esistesse una chiave con nome uguale, nel dizionario esiste la funzione: <Nome Dizionario>.setdefault(<Nome Chiave>, <Nome Elemento>)

print("Sesto Print:")

print("Cibo in frigo:", list(food_in_fridge.items()))
food_in_fridge.setdefault("Beer", "Moretti")
print("Dopo l'aggiunta della birra:", list(food_in_fridge.items()))

#Le righe di codice sottostanti non vengono eseguite poiché esiste già, nel dizionario "food_in_fridge", un elemento con chiave "Vegetables"

print("Settimo Print")

food_in_fridge.setdefault("Vegetables", "Cucumber")
print("Cibo in frigo:", list(food_in_fridge.items()))

#Le righe di codice sottostanti invece modificano il dizionario "food_in_fridge" aggiungendo l'elemento "Cucumber" ad una chiave già esistente

print("Ottavo Print")

lista_frutti = food_in_fridge["Fruits"]
lista_frutti.append("Cucumber")
food_in_fridge["Fruits"] = lista_frutti
print(food_in_fridge)

