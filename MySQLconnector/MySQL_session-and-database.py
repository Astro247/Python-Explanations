'''
Per potersi connettere ad una sessione, ossia ad un server contenente uno o più database, è necessario utilizzare la funzione ".connect()"
Che prende come keyword argument l'ip (nome dell'host) a cui connettersi, il nome utente, la password e eventualmente anche la porta.
Se il database è già stato creato ed è già presente all'interno della sessione, è sufficiente inserire il nome del database come valore del keyword argument "database".
'''

import mysql.connector as mysql

connection = mysql.connect(
    host = "localhost", #L'abbreviazione "localhost", oppure l'ip 127.0.0.1, si riferisce al server contenente i database del computer, quindi in locale.
    user = "root", #con "user" si intende "nome_utente"
    password = "pass", #Password per connetersi alla sessione
    database = "db_python" #Nome del database (campo "extra" in quanto è sufficiente prima di ogni tanto inserire i keyword arguments inerenti alla sessione)
)      

if connection.is_connected(): #La funzione ".is_connected()" ritorna un valore booleano "True" qualora la connessione al database/sessione sia avvenuta con successo, mentre ritorna un valore "False" se la connessione non è stata stabilita oppure è stata chiusa.
    print("The connection has been established.")
else:
    print("Something went wrong..")


'''
Qualora il database non esistesse, è necessario prima connettersi alla sessione e successivamente creare il database, per poi connettersi
ad esso.

Dopo essersi connessi con successo alla sessione, è necessario creare un "cursor", ossia un oggetto iterabile che restituisce, una riga
alla volta, i risultati di una query, e ogni riga è rappresentata come una tupla.

Con la funzione ".execute()" è possibile scrivere ed eseguire query SQL il cui risultato verrà salvato all'interno della variabile assegnata
alla funzione "<nome_connessione>.cursor()".
'''

connection = mysql.connect(
    host="localhost",
    user="root",
    password="pass",
)

if connection.is_connected(): #Verifica che ci siamo connessi alla sessione.
    print("The connection has been established.")
else:
    print("Something went wrong..")

cursor = connection.cursor() #Abbiamo creato un cursore e assegnato alla variabile "cursor", ora è possibile, riferendosi con delle funzioni a questa variabile, scrivere e mostrare a schermo risultati di query sql.

cursor.execute("CREATE DATABASE IF NOT EXISTS db_python") #Con questa query, abbiamo creato il database "db_python"

connection.database = "db_python" #Adesso ci stiamo connettendo al nuovo database.

cursor.execute("SHOW DATABASES()") #Con questa query abbiamo salvato dentro la variabile "cursor" una tabella (con una sola colonna) contenente il nome dei database presenti nella sessione.

print("Databases list:")
for database in cursor: #Ciclando per ogni riga dell'unica colonna (quindi nell'indice 0 dell'unica colonna presente) e printando a schermo "database[0]" stiamo printando il nome dei database presenti nella tabella.
    if database[0] == "db_python":
        print("-", database[0], " <-- New Database")
    else:
        print("-", database[0])

'''
Una volta creato il database all'interno della sessione ed aver verificato che sia stato creato o meno, è utile verificare se si è attualmente
connessi a quello specifico database.

Per farlo, basta eseguire la query "SELECT DATABASE()" che chiede a MySQL quale database è attualmente in uso in quella connessione.
In quanto il risultato verrà salvatto come tabella nella variabile cursor, in quanto si tratterà di una tabella contenente una sola riga,
ossia il nome del database, basterà utilizzare la funzione del cursor ".fetchone()" che ritorna il nome del database attualmente in uso.

La funzione ".fetchone()" seleziona una sola riga nella tabella risultato del cursor una volta che una query è stata eseguita.
'''

cursor.execute("SELECT DATABASE()") #Esegue lo scan del database attualmente in uso.

current_database = cursor.fetchone() #Estrapola il risultato della query, in particolare una sola riga, in questo caso l'unica riga, della tabella creata come risultato della query.

print("Database attualmente selezionato:", current_database[0])