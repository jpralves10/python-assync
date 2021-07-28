from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


produtos = [
    Produto(id=1, nome='1', preco=12.0, em_oferta=True),
    Produto(id=2, nome='2', preco=22.0, em_oferta=True),
    Produto(id=3, nome='3', preco=32.0, em_oferta=True),
    Produto(id=4, nome='4', preco=42.0, em_oferta=False),
    Produto(id=5, nome='5', preco=52.0, em_oferta=False),
]
