#Le liste sono simili agli array, con la differenza che in questo caso possono contenere qualsiasi tipo di dato al loro interno.

print("Primo Print:")
my_list = [1,2,"abc",3.5]
print(my_list)

#Come per gli array, gli elementi nelle liste sono catalogati da un'indice:

print("Secondo Print:")
print("Primo e Terzo elemento:", my_list[0], my_list[2])

#Per sortare alfabeticamente o numericamente il contenuto di una lista si utilizza il comando: <Nome Lista>.sort

print("Terzo Print:")
second_list = [3,5,7,5.2,8]
print("Ecco una lista di numeri:", second_list)
second_list.sort()
print("Ecco la lista ordinata:", second_list)
second_list.sort(reverse=True)
print("Ecco la lista ordinata al contrario:", second_list)

#Per selezionare un range di elementi della lista si separano l'indice iniziale e quello finale da un ":", dove l'indice finale non è incluso, mentre quello iniziale sì 

print("Quarto Print:")
print("Ecco gli elementi della lista:", my_list[:])
print("Ecco gli elementi dal secondo in poi:", my_list[1:])
print("Ecco gli elementi dal secondo al terzo:", my_list[1:3])

#Per sostituire un'elemento di una lista con un'altro, basta modificarlo con assegnazione specificando l'indice di quell'elemento

print("Quinto Print:")
third_list = [1,2,3]
print("Ecco la lista iniziale:", third_list)
third_list[0] = "Uno"
print("Ecco la lista finale:", third_list)

#Per aggiungere un nuovo elemento in una lista si utilizza il comando: <Nome Lista>.append

print("Sesto Print:")
print("Ecco la lista iniziale:", third_list)
third_list.append("Quattro")
print("Ecco la lista con elementi in più:", third_list)

#Per rimuovere un'elemento da una lista ci sono diversi modi:
#Per rimuovere l'ultimo elemento si utilizza il comando: <Nome Lista>.pop()
#Per rimuovere uno specifico elemento in una lista si utilizza il comando: <Nome Lista>.remove(Nome Elemento)
#Per rimuovere un elemento in una lista selezionandolo con l'indice si utilizza il comando: del <Nome Lista>[indice dell'elemento]

print("Settimo Print:")
fourth_list = [1,2,3,4,5,6,7,8]
print("Ecco la lista iniziale:", fourth_list)
fourth_list.pop()
print("Ecco la lista senza l'ultimo elemento:", fourth_list)
fourth_list.remove(4)
print("Ecco la lista senza il numero \"4\":", fourth_list)
del fourth_list[0]
print("Ecco la lista senza il primo elemento:", fourth_list)

#Per ricavare l'indice di un'elemento nella lista si utilizza il comando: <Nome Lista>.index(elemento)

print("Ottavo Print:")
fifth_list = ["ciao","mi","chiamo","paolo"]
print("La parola \"mi\" è in posizione:", fifth_list.index("mi"))