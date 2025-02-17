#Le f_string permettono di assegnare a una variabile il valore stringa pur inserendo a quest'ultima qualsiasi tipo di dato al suo interno

print("Primo Print:")
num = 1
nome = "Giacomo"
numero_uno = "sono " + nome + "e sono il numero " + str(num)
print(numero_uno)
numero_uno = f"sono {nome} e sono il numero {num}, e la somma di {num} e 2 fa {num + 2}"
print(numero_uno)

#La funzione "<Nome stringa>.startswith(parametro)" ritorna un valore booleano True se la stringa inizia con il parametro inserito
#Analogamente la funzione "<Nome stringa>.endswith(parametro)" ritorna un valore booleano True se la stringa finisce con il parametro inserito


print("Secondo Print:")
frase = "Ciao mi chiamo massimo"
if frase.startswith("Ciao"):
    frase_finale = "e ti ho salutato"
    print(frase + " " + frase_finale)
if frase.endswith("massimo"):
    print("Come stai?")

#La funzione .isalnum() ritorna un valore booleano verificando che in una stringa siano contenuti solo valori alfa-numerici (esclusi gli spazi)
#La funzione .isalpha() verifica che una stringa sia composta solo da caratteri alfabetici, mentre la funzione .isdecimal() solo da caratteri numerici, ritornando sempre un valore booleano (esclusi gli spazi)
#Infine, la funzione .isspace() verifica che una stringa sia composta solo da caratteri " ", ritornando un valore booleano.

print("Terzo Print:")
stringa_uno = "SonoMarcoEdHo18Anni"
stringa_due = "NonsiLancianoGliOggetti"
stringa_tre = "1935"
stringa_quattro = " "
if stringa_uno.isalnum():
    print("La stringa \"" + stringa_uno + "\", contiene sia caratteri alfabetici che numerici")
if stringa_due.isalpha():
    print("La stringa \"" + stringa_due + "\" contiene solo caratteri alfaberici")
if stringa_tre.isdecimal():
    print("La stringa \"" + stringa_tre + "\" contiene solo caratteri numerici")
if stringa_quattro.isspace():
    print("Infine la stringa \"" + stringa_quattro + "\" contiene solo spazi")

#La funzione .upper() modifica i caratteri alfabetici di una stringa in maiuscolo
#La funzione .lower(), invece, modifica i caratteri alfabetici di una stringa in minuscolo

print("Quarto Print:")
stringa_minuscola = "ciao"
print("in maiuscolo la stringa '" + stringa_minuscola + "' diventa '" + stringa_minuscola.upper() + "'")
stringa_maiuscola = "CIAO"
print("Viceversa la stringa '" + stringa_maiuscola + "' diventa '" + stringa_maiuscola.lower() + "'")

#Per collegare gli elementi di una lista in una stringa si utilizza la funzione: "'<Carattere intermediario>'.join(<Nome Lista>)"
#Viceversa per separare gli elementi di una stringa e inserirli in una lista si utilizza la funzione: "<Nome stringa>.split(<Carattere intermediario>)"

print("Quinto Print:")
lista = ["ciao", "mi", "chiamo", "massimo"]
print(" ".join(lista))
stringa = "ho tanti anni"
print(stringa.split(" "))

#Per calcolare il numero di caratteri che compongono una stringa si utilizza la funzione: "len(<Nome Stringa>)"
#Per le liste, invece, la funzione len restituisce il numero di elementi nella lista.
#In entrambi i casi, in quanto la lunghezza è un numero, il valore restituito è un intero.

print("Sesto Print:")
lista = ["oggi", 2, 5.5]
stringa = "gigante"
print("La lista contiene", len(lista), "elementi, mentre la stringa contiene", len(stringa), "caratteri")