
# Per visualizzare il risultato ho utilizzato uvicorn "uvicorn 'nome-file-py':'nome-app' --reload (reload aggiorna il server in tempo reale)".

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

test = FastAPI()
items = []


# A differenza di Flask, il decoratore sostituisce direttamente 'route' con il method.
@test.get('/')
def homepage():
    return "Hello world"


# codice da terminale per inviare una richiesta HTTP: curl.exe -X POST -H "Content-Type: application/json" '(URL)/items?item=test-item' (curl.exe -X POST -H "Content-Type: application/json" '[URL]/items?item=[test-item]')
# "curl.exe", su windows, serve per fare una richiesta http, "-X POST" specifica il metodo della richiesta, in questo caso POST, "-H" indica l'header della richiesta, in questo caso è un file json e nella route 'URL/items' con il simbolo '?', usato per inviare un dato, viene assegnato al parametro 'item' il valore 'test-item'.
@test.post('/items')
def add_items(item: str):
    items.append(item)
    return items
