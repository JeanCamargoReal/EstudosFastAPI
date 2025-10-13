from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Optional

app = FastAPI()


# 1. CRIAMOS A NOSSA CLASSE DE DEPENDÊNCIA
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        # O FastAPI vai injetar os parâmetros de query aqui.
        self.q = q
        self.skip = skip
        self.limit = limit


# 2. USAMOS A CLASSE COMO DEPENDÊNCIA
# Note que passamos a CLASSE, não uma instância dela.
# FastAPI se encarregará de criar a instância para nós.
app.get("/items/")


# `commons` será uma INSTÂNCIA da classe CommonQueryParams.
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    # Agora podemos acessar os parâmetros como atributos da instância.
    return {"message": "Lista de Itens", "params": commons}


@app.get("/users/")
async def read_users(commons: CommonQueryParams = Depends()):  # Forma abreviada
    # Se a 'type hint' (CommonQueryParams) é a dependência,
    # você pode usar apenas Depends() como atalho.
    return {"message": "Lista de Usuários", "params": commons}


# DEPENDÊNCIA 1: Obtém o token do header
async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header inválido")
    return x_token


# DEPENDÊNCIA 2: Obtém o usuário, MAS PRECISA DO TOKEN
# Note como ela própria usa `Depends` para declarar sua necessidade.
async def get_current_user(token: str = Depends(get_token_header)):
    # Em um app real, você decodificaria o token e buscaria o usuário no banco.
    # Aqui vamos apenas simular.
    user = {"username": "fakeuser", "token_used": token}
    return user


# ROTA FINAL
# Nossa rota só precisa se preocupar com o que ela quer: o usuário atual.
# Ela não precisa saber sobre tokens ou headers.
@app.get("/users/me")
async def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
