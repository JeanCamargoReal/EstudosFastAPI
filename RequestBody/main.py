from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    # Se o código chegou a este ponto, o FastAPI já fez tudo por você.
    # 'item' não é um dicionário, é uma instância real da sua classe 'Item'.
    
    # Você pode acessar os dados com autocomplete e segurança de tipos.
    print(f"Nome do item: {item.name}")
    print(f"Preço do item: {item.price}")

    # A resposta também pode ser o próprio objeto. FastAPI o converterá para JSON.
    item_criado = item.model_dump()
    item_criado.update({"message": "Item criado com sucesso!"})
    return item_criado