from fastapi import FastAPI

app = FastAPI()

# Nosso "banco de dados" em memória para exemplo
fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
    {"item_name": "Qux"},
    {"item_name": "Lorem"},
    {"item_name": "Ipsum"},
]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    # 'skip' e 'limit' não estão em "/items/", logo são parâmetos de query.

    # Adicionamos valores padrão (skip=0, limit=10).
    # Isso os torna OPCIONAIS. Se o cliente não os enviar, esses valores serão usados.

    return fake_items_db[skip : skip + limit]
