#Le funzioni rappresentano del codice riutilizzabile efficientemente, una funzione prende il nome di: "def <Nome Funzione>(<Nome Parametri>):"
#I parametri sono delle variabili fantasma esistenti solo all'interno della funzione, richiamabili con altri valori, o altre variabili, altrove nel codice.
#Se una funzione non ritorna niente viene classificata come "NoneType", pertanto, se si vuole ritornare qualcosa in output, è necessario mettere un return alla fine del codice nella funzione

print("Primo Print:")
def somma():
    a = int(input("Inserire a = "))
    b = int(input("Inserire b = "))
    risultato = a+b
    return risultato
print("La somma fra a e b è", somma())

#Il valore di che ritorna la funzione può essere assegnato a una variabile al di fuori della funzione

print("Secondo Print:")
def modifica(val):
    a = int(input("Inserire il valore di a = "))
    val = val+a
    return val
b = int(input("Inserire il valore di b = "))
c = modifica(b)
print("Il risultato è", c)
