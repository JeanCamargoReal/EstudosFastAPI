from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Post(BaseModel):
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=10)

# "Banco de dados"
db_posts = {
    1: Post(title="Aprendendo FastAPI", content="Esta é a primeira aula..."),
    2: Post(title="Dominando Pydantic", content="Modelos de dados são importantes")
}

@app.get("/posts/{post_id")
async def get_post(post_id: int):
    # Lógica de negócio: o post existe?
    if post_id not in db_posts:
        # Se não existe, levante um erro 404
        raise HTTPException(status_code=404, detail=f"Post com ID {post_id} não encontrado.")

    return db_posts[post_id]

@app.post("/posts/", status_code=201) # status_code=201 informa o código de sucesso
async def create_post(post: Post):
    # Lógica de negócio: o título já está em uso?
    for existing_post in db_posts.values():
        if existing_post.title == post.title:
            # Se já existe, levante um erro 409 Conflict
            raise HTTPException(status_code=409, detail="Um post com este título já existe.")

    new_id = max(db_posts.keys() or [0]) + 1
    db_posts[new_id] = post
    return {"message": "Post criado com sucesso", "post_id": new_id}
