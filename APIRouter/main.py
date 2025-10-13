from fastapi import FastAPI
from routers import items, users

app = FastAPI()

# 1. Inclua o router de usuários
app.include_router(users.router, prefix="/users", tags=["Users"])

# 2. Inclua o router de itens
app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/")
async def root():
    return {"message": "API Principal"}
