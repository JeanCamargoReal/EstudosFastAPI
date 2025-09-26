from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Nosso "banco de dados" em memória para o exemplo
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
    # 'skip' e 'limit' não estão em "/items/", logo são parâmetros de query.

    # Adicionamos valores padrão (skip=0, limit=0).
    # Isso os torna OPCIONAIS. Se o cliente não os enviar, esses valores serão usados.

    return fake_items_db[skip : skip + limit]


@app.get("/items_search/")
async def search_items(q: Optional[str] = None):
    # 'q' é um parâmetro de query opcional que deve ser uma string.

    results = {"message": "Buscando por todos os items"}

    if q:
        # Se o cliente enviou o parâmetro 'q' (ex: /items_search/?=foo),
        # ele não será None e entraremos neste if.
        results.update({"query_recebida": q})

    return results


@app.get("/items/{item_id}")
async def read_item_details(item_id: int, show_details: bool = False):
    # 'item_id' é um Parâmetro de Rota
    # 'show_details' é um Parâmetro de Query booleano opcional

    item = {"item_id": item_id, "name": f"Item {item_id}"}

    if show_details:
        item.update({"description": "Esta é uma descrição detalhada do item."})

    return item
