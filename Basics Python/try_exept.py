#L'istruzione try analizza il codice che lo contiene, se quest'ultimo ritorna un'errore allora viene eseguito il codice all'interno dell'istruzione except

print("Primo Print:")

var = input("Inserisci un numero: ")

try:
    var = int(var)
except:
    while True:
        var = input("Ciò che hai inserito non è un numero, reinserire: ")
        try:
            var = int(var)
            break
        except:
            continue

#Un singolo try possono essere associati più except e ad ogni except può essere specificato il tipo di errore che deve analizzare in caso si riscontri nel try

print("Secondo Print:")

var = input("Inserisci un numero diverso da zero: ")

try:
    var = int(var)
    result = 1/var
except:
    while True:
        try:
            var = int(var)
            result = 1/var
            break
        except ZeroDivisionError:
            var = input("Hai inserito zero, ripetere: ")
            continue
        except ValueError:
            var = input("Non hai inserito un numero, ripetere: ")
            continue

#L'istruzione "finally" esegue un blocco di codice indipendentemente dal fatto che il blocco di codice nell'except venga letto oppure no.

print("Terzo Print:")

var = "Stringa"
try:
    intero = var + 1
except TypeError:
    print("Sono entrato nell'except")
finally:
    print("Avanti (parte 1)")

var = 5
try:
    intero = var + 1
except TypeError:
    print("Sono entrato nell'except")
finally:
    print("Avanti (parte 2)") 