from fastapi import FastAPI
from pydantic import BaseModel

test = FastAPI()

# A differenza di una classe qualunque, il BaseModel di pydantic, oltre a convertire i dati nel tipo giusto ("123" => 123), assicura che il tipo di dato inserito nel file json dal client corrisponda a quello inserito originariamente nella classe.


class User(BaseModel):
    username: str = None
    age: int = None

# Nella powershell di windows, il comando per far sì che il client possa inviare al server un file json: (curl.exe -X POST -H "Content-Type: application/json" -d '{\"username\":\"ciao\", \"age\":15}' [URL]/insertUser) Su windows, dato che chiavi e valori non interi sono fra doppi apici, per non scombussolare la powershell si inseriscono anche diversi '\' nella configurazione del file json.


@test.post('/insertUser')
def add_user(user: User):
    return user
