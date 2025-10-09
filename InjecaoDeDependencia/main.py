from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()


# 1. CRIAMOS A NOSSA DEPENDÊNCIA
# Esta é uma função normal, mas o FastAPI irá tratá-la de forma especial.
# Ela pode receber seus próprios parâmetros (de rota, query, etc.).
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


# 2. USAMOS A DEPENDÊNCIA NAS NOSSOAS ROTAS


@app.get("/items/")
# O parâmetro `commons` receberá o dicionário retornado por `common_parameters`.
async def read_items(commons: dict = Depends(common_parameters)):
    # Agora `commons` é um dicionário contendo os parâmetros da query.
    return {"message": "Lista de Itens", "params": commons}


@app.get("/users/")
# Reutilizamos a mesa dependência aqui! Sem repetir código.
async def read_users(commons: dict = Depends(common_parameters)):
    return {"message": "Lista de Usuários", "params": commons}
