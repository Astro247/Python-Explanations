#Numpy amplia di molto i tipi di dati che le variabili possono assumere.
#Alcuni tipi di dato, come gli array di interi, vengono accompagnati da un numero, qualora si volesse printare il loro type, che rappresenta il numero di bit che quell'array occupa nella memoria.

#Il metodo "dtype" è utile se si volesse specificare il tipo di dato che un'array deve assumere, oppure solamente per capire di che tipo di dato è un'array.

import numpy as np

print("\nFirst Print:\n")

arrInt = np.array([1,2,3,4,5])
arrStr = np.array([1,2,3,4,5], dtype='S') #Pper specificare il tipo di dato di un'array, il metodo dtype viene passato alla funzione come keyword argument. In questo caso 'S' sta per 'Stringa'

print(f"First Array Type: {arrInt.dtype}")
print(f"First Array Type: {arrStr.dtype}")

#Il metodo "astype" permette la modifica del tipo di dato che un'array deve assumere dopo la sua assegnazione a una variabile, a differenza di "dtype" che esegue questo processo duranet la sua assegnazione.

print("\nSecond Print:\n")

arrInt = np.array([1,2,3,4,5])
print(f"This array it's an '{arrInt.dtype}' type variable: {arrInt}")

arrInt = arrInt.astype('S')
print(f"The same array it's now a '{arrInt.dtype}' type variable: {arrInt}")

#Le assegnazioni di un tipo specifico di dato ad una variabile array con il metodo "dtype" possono avvenire solo qualora tutti gli elementi dell'array siano di uno specifico tipo o possono essere trasformati in tale.

print("\nThird Print:\n")

try:

    arrInt = np.array([1,"a",3], dtype='i')
    print(f"Array type: {arrInt.dtype}")

except ValueError:
    print("Since the array contains a char and a integer value, the array can't be an integer type.")

#Come detto all'inizio, esistono diversi tipi di dato assegnabili agli array, fra cui:

print("\nFourth Print:\n")

#1) Interi, assegnati con 'i' (oppure int): può contenere valori interi.

arr = np.array([1, 2, 3])
print(f"Array type: {arr.dtype} = ({arr})")

#2) Float, assegnati con 'f': può contenere 

arr = np.array([1.1, 2.2, 3.3])
print(f"Array type: {arr.dtype} = ({arr})")

#2) Boolean, assegnati con 'bool': può contenere "True" o "False".
#se dovesse essere trasformato con il metodo "dtype" da intero a booleano, gli elementi contenuti nell'array funzionano esattamente come qualsiasi variabile booleana (quindi se diverso da zero allora True, mentre se uguale a zero è False)

arr = np.array([True, False, True])
print(f"Array type: {arr.dtype} = ({arr})")

arr = np.array([52, -8, 0], dtype='bool')
print(f"Array type: {arr.dtype} = ({arr})")

#3) Intero Senza Segno, assegnato con 'uint': può contenere solo interi senza segno (quindi solo numeri interi positivi)

try:

    arr = np.array([-1, 3, -6], dtype='uint')
    print(f"Array type: {arr.dtype} = ({arr})")

except OverflowError:

    arr = np.array([1, 3, 6], dtype='uint')
    print(f"Array type: {arr.dtype} = ({arr})")

#4) Numeri Complessi, assegnato con 'complex64' oppure 'complex128': può contenere anche numeri interi con una parte immaginaria (la parte immaginaria è specificata con 'j', non con 'i').
#Tutti gli elementi hanno una parte immaginaria, anche se non specificata dall'utente.

arr = np.array([1, 3+2j, -6], dtype='complex64')
print(f"Array type: {arr.dtype} = ({arr})")

#5) Oggetto, assegnato con 'O': può contenere qualsiasi tipo di dato.

arr = np.array([-1, 3+2j, "a", "ab", 6, True, 5.5], dtype='O')
print(f"Array type: {arr.dtype} = ({arr})")

#6) Stringa, assegnato con "S": stringa che può supportare solo i a caratteri ASCII e utilizza un byte per carattere.

try:

    arr = np.array(["é", "hello", "ひ"], dtype='S')
    print(f"Array type: {arr.dtype} = ({arr})")

except UnicodeEncodeError:

    arr = np.array(["hello", "world"], dtype='S')
    print(f"Array type: {arr.dtype} = ({arr})")

#7) Stringa Unicode, assegnato con "U": stringa che può supportare tutti i caratteri Unicode (qualsiasi tipo di carattere), ma utilizza quattro byte per carattere.

arr = np.array(["é", "hello", "ひ"], dtype='U')
print(f"Array type: {arr.dtype} = ({arr})")