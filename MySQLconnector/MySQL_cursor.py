'''
Il cursor e' una funzione della variabile associata alla sessione a cui si è collegati, ed è possibile 
associare ad essa diverse funzioni:

La funzione ".execute()" permette di eseguire direttamente una query fissa, cioè una query completa che non richiede valori esterni.
In questo caso, basta inserire la query come unico argomento, scritta sotto forma di stringa.
Se invece la query contiene valori esterni da inserire, allora si usa un secondo argomento, che è una lista o tupla di valori.
In questo caso, all’interno della stringa della query si inseriscono i segnaposto '%s' nei punti dove andranno inseriti i valori.
I valori passati nel secondo argomento saranno inseriti nell’ordine in cui compaiono i segnaposto.

A differenza della funzione ".execute()", la funzione ".executemany()" contiene un tipo di query che richiede valori esterni come stringa,
ma vi è possibile inserire come secondo positional argument una lista di liste per inserire più valori in una sola istruzione.

Tutte le volte che una query dinamica, quindi che richiede valori esterni, è stata scritta con la funzione ".execute()" è necessario
salvare quei dati nel database con la funzione ".commit()"

Per poter osservare i risultati salvati nel cursor con la funzione ".execute()" o ".executemany()" è possibile utilizzare la funzione "fetch",
ossia "raccogli", ma in particolare ".fetchall", ossia "raccogli tutto", raccoglie tutte le righe di una tabella.
La funzione ".fetchone" invece, ossia "raccogli uno" si limita a prendere una sola riga data dalla query e non di più.

La funzione ".rowcount()" invece restituisce un valore numerico rappresentante il numero di righe trovate nella tabella generata
dalla query salvata nel cursor.
'''

import mysql.connector as mysql

connection = mysql.connect(
    host = "localhost",
    name = "root",
    password = "pass"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS cursor_database")
connection.database("cursor_database")

cursor.execute("""CREATE TABLE IF NOT EXISTS utenti (
               id INT NOT NULL AUTO_INCREMENT,
               nome VARCHAR(50) NOT NULL,
               email VARCHAR(50) NOT NULL, 
               PRIMARY KEY(id)
               )""") #Anche se la query è lunga, non ci sono inserimenti dinamici in input, ed essendo dunque tutti valori statici è sufficienet una singola ".execute"

valori = [
          ("Luca", "Lucabello@hotmail.com"),
          ("Marco", "Marcolino53@gmail.com"), 
          ("Elia", "Elia_sas@libero.it")
          ]

cursor.executemany("INSERT TABLE utenti (nome, email) VALUES (%s, %s)", valori) #In questo caso ci sono valori in input da inserire e sono più valori su più righe, pertanto è stato necessario utilizzare un ".executemany" e come secondo positional argument è stata inserita una lista di tuple.

connection.commit() #Avendo inserito valori in input, abbiamo salvato e aggiornato il database.

cursor.execute("SELECT * FROM utenti")

print(f"Tutte le righe della tabella:\n {cursor.fetchall()}") #Dato che abbiamo eseguito una query selezionando più righe, per poterle vedere tutte è necessario utlizzare ".fetchall"

cursor.execute("SELECT * FROM utenti WHERE id = 1")

print(f"Prima riga della tabella:\n {cursor.fetchone()}") #In questo caso, invece, avendo selezionato una sola riga, basta utilizzare ".fetchone"

cursor.execute("SELECT * FROM utenti WHERE id%1!=0")

print(f"Numero colonne con ID dispari: {cursor.rowcount}") #Questa funzione non stampa le righe selezionate nella query, ma il numero di righe.