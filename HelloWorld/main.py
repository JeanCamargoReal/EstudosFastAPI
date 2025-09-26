from fastapi import FastAPI, HTTPException

app = FastAPI()

# Nosso "banco de dados" em memória
db_items = {1: "Maçã", 2: "Banana", 3: "Laranja"}


# --- OPERAÇÕES DE LEITURA (Read) para um item específico ---


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Recupera um item específico pelo seu ID.
    """
    if item_id not in db_items:
        # Se o item não existe, retornamos um erro 404
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return {"id": item_id, "name": db_items[item_id]}


# --- OPERAÇÃO DE ATUALIZAÇÃO (Update) para um item específico


@app.put("/items/{item_id}")
async def update_item(item_id: int):
    """
    Atualiza um item específico pelo seu ID.
    """
    if item_id not in db_items:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    # Simula a atualização
    db_items[item_id] = f"Item {item_id} Atualizado"

    return {
        "message": "Item atualizado com sucesso",
        "item": {"id": item_id, "name": db_items[item_id]},
    }


# --- OPERAÇÃO DE DELEÇÃO (Delete) para um item específico ---


@app.delete("/item/{item_id}")
async def delete_item(item_id: int):
    """
    Remove um item específico pelo seu ID
    """
    if item_id not in db_items:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    del db_items[item_id]
    # Uma boa prática para DELETE é retornar uma resposta vazia com status 204 No Content
    # Mas para fins didáticos, vamos retornar uma mensagem.
    return {"message": "Item removido com sucesso"}
