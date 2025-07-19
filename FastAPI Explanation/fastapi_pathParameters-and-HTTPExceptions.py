from fastapi import FastAPI, HTTPException

test = FastAPI()
items = []

# Dopo aver specificato la route "/items" la route "{items_id}" è un "path parameter", quindi quella path accetta un valore, in questo caso numerico, dinamico. (curl.exe -X GET "[URL]/numItems/[num]")
# Per rendere più chiari gli errori si può importare HTTPException da fastapi. Per printare un'errore, si utilizza la keyword "raise" seguito dall'estensione HTTPExceptation e come suoi keyword arguments si può inserire lo status code e dei dettagli sull'errore.


@test.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404,
                            detail=f"ID item {item_id} is not on the list")


# Questo è un'altro esempio di path parameter, ma in questo caso, di default, l'intero "limit" è impostato a 10
@test.get('/numItems/{limit}')
def count_items(limit: int = 10):
    return items[0:limit]
