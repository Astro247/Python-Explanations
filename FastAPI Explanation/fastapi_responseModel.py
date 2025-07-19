from fastapi import FastAPI
from pydantic import BaseModel


class userIn(BaseModel):
    username: str
    password: str


class userOut(BaseModel):
    username: str


app = FastAPI()


@app.post("/register", response_model=userOut)
def registerUser(userModel: userIn):
    return userModel

# Nonostante userModel sia assegnato al BaseModel "userIn", e di conseguenza a riga 19 dovrebbero ritornare tutti i dati inseriti dal client, siccome il response_model è assegnato a "userOut", vengono mostrati solo le chiavi-valori presenti in entrambe le classi.
# In altre parole il response_model è il modello con cui il server risponde al client, quindi il server invia al client uno specifico API filtrato in base al response_model.
