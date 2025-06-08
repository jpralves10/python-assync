"""
pip install fastapi uvicorn[standard]

* Para subir o servidor:
uvicorn main:app --reload
"""

from fastapi import FastAPI

from produto import produtos, Produto

app = FastAPI(title='teste')


@app.get('/')
async def index():
    return {"mensage": "hello world!"}


@app.get('/produtos/{id}')
async def get_produto(id: int):
    for produto in produtos:
        if id == produto.id:
            return produto
        return None

@app.put('/produtos/{id}')
async def put_produto(id: int, produto: Produto):
    for prod in produtos:
        if id == produto.id:
            prod = produto
            return prod



# para rodar: uvicorn --host 0.0.0.0 --port 8080 main:app --reload
