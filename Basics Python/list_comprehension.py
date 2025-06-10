# E' possibile creare una lista riferendosi ad altre liste senza usare più di una riga di codice:

list = [1,2,2,5,7,2,1,9]
even = [num for num in list if num%2==0]
print(even)

#La sintassi è questa:

# "num for num in list" itera, con 'num' come contatore, itera per ogni elemento della lista 'list' e per ogni elemento, se non dovesse esserci scritto nient'altro, fai un 'even = list.append(num)'
# "if num%2==0" invece di fare un .append mettendo ogni elemento di 'list' dentro 'even', metti nella lista 'even' solo gli elementi che rispettano la condizione dell'if.