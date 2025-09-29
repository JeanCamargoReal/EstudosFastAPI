from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    # Obrigatório (...), com no mínimo 3 caracteres.
    name: str = Field(..., min_length=3)

    # Obrigatório (...), estritamente maior que 0.
    price: float = Field(..., gt=0, description="O preço não pode ser negativo.")

    # Opcional (valor padrão None), com no máximo 300 caracteres.
    description: Optional[str] = Field(None, max_length=300)

    # Opcional (valor padrão None), maior ou igual a 0
    tax: Optional[float] = Field(None, ge=0)


# Simula banco de dados
db_items = {}

@app.put("/items/{item_id}")
async def update_item(*, # O '*' força os argumentos seguintes a serem apenas nomeados (keyword-only)
                      item_id: int = Path(..., title="O ID do item a ser atualizado", gt=0),
                      notify_user: bool = Query(True, description="Envia notificação ao usuário?"),
                      item: Item):
    if item_id not in db_items:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    db_items[item_id] = item.dict()
    return {"item_id": item_id, "updated_item": item, "notificacao_enviada": notify_user}

@app.post("/items/")
async def create_item(item: Item):
    novo_id = len(db_items) + 1
    db_items[novo_id] = item.dict()
    return {"message": "Item criado", "item_id": novo_id, "item_data": item}

@app.get("/search/")
# O primeiro argumento de Query é o valor padrão.
# '...' (Ellipsis) indica que o parâmetro é obrigatório.
async def search_items(q: str = Query(..., min_length=3, max_length=50)):
    return {"query": q}

@app.get("items/{item_id")
# Obrigatório (marcado com '...') e maior que 0.
# gt=0: "Greater Than" 0. O valor deve ser estritamente maior que 0.
# le=1000: "Less Than or Equal" 1000. O valor deve ser menor ou igual a 1000.
# Outras opções numéricas: ge (maior ou igual), lt (menor que).
async def read_item(item_id: int = Path(..., gt=0, le=1000)):
    return {"item_id": item_id}