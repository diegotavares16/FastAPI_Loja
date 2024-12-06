from fastapi import FastAPI
from produtos import Produto, ProdutoDB

app = FastAPI()

produto_db = ProdutoDB("produtos.json")

@app.get('/produtos', tags=['produtos'])
def listar_produtos():
    """Listar todos os produtos"""
    produtos = produto_db.carregar_dados()
    return produtos

@app.get('/produtos/disponiveis', tags=['produtos'])
def listar_produtos_disponiveis():
    """Listar produtos disponíveis"""
    produtos_disponiveis = produto_db.listar_produtos_disponiveis()
    return produtos_disponiveis

@app.get('/produtos/{produto_id}', tags=['produtos'])
def obter_produto(produto_id: int):
    """Obter produto"""
    produto = produto_db.obter_produto(produto_id)
    return produto

@app.post('/produtos', tags=['produtos'])
def criar_produto(produto: Produto):
    """Criar produto"""
    novo_produto = produto_db.adicionar_produto(produto)
    return novo_produto

@app.put('/produtos/{produto_id}', tags=['produtos'])
def atualizar_produto(produto_id: int, produto_novo: Produto) -> dict:
    """Atualizar produto"""
    produto_atualizado = produto_db.atualizar_produto(produto_id, produto_novo)
    return produto_atualizado

@app.delete('/produtos/{produto_id}', tags=['produtos'])
def deletar_produto(produto_id: int):
    """Deletar produto"""
    resposta = produto_db.remover_produto(produto_id)
    return resposta
