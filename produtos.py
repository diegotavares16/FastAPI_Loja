import json
from typing import Optional
from pydantic import BaseModel

class Produto(BaseModel):
    """Classe de produto"""
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: Optional[bool] = True


class ProdutoDB:
    """Classe para manipular o banco de dados JSON"""
    def __init__(self, caminho: str):
        self.caminho = caminho

    def carregar_dados(self) -> list:
        """Carrega os dados do arquivo JSON"""
        with open(self.caminho, "r") as f:
            return json.load(f)["produtos"]

    def salvar_dados(self, produtos: list):
        """Salva os dados no arquivo JSON"""
        with open(self.caminho, "w") as f:
            json.dump({"produtos": produtos}, f, indent=4)

    def adicionar_produto(self, produto: Produto) -> dict:
        """Adiciona um produto ao banco de dados"""
        produtos = self.carregar_dados()
        novo_produto = produto.dict()  
        novo_produto["id"] = max(p["id"] for p in produtos) + 1 if produtos else 1  
        produtos.append(novo_produto)
        self.salvar_dados(produtos)
        return novo_produto

    def atualizar_produto(self, produto_id: int, produto_novo: Produto) -> dict:
        """Atualizar produto"""
        produtos = self.carregar_dados()
        
        for produto in produtos:
            if produto["id"] == produto_id:
                produto["nome"] = produto_novo.nome
                produto["descricao"] = produto_novo.descricao
                produto["preco"] = produto_novo.preco
                produto["disponivel"] = produto_novo.disponivel
                self.salvar_dados(produtos)
                return produto
        
        return {"erro": "Produto não encontrado"}

    def obter_produto(self, produto_id: int) -> dict:
        """Obter um produto pelo ID"""
        produtos = self.carregar_dados()
        for produto in produtos:
            if produto["id"] == produto_id:
                return produto
        return {"erro": "Produto não encontrado"}

    def remover_produto(self, produto_id: int) -> dict:
        """Remove um produto pelo ID"""
        produtos = self.carregar_dados()
        
        for produto in produtos:
            if produto["id"] == produto_id:
                produtos.remove(produto)
                self.salvar_dados(produtos)
                return {"mensagem": "Produto removido com sucesso"}
        
        return {"erro": "Produto não encontrado"}

    def listar_produtos_disponiveis(self) -> list:
        """Lista apenas os produtos disponíveis"""
        produtos = self.carregar_dados()
        return [produto for produto in produtos if produto["disponivel"]]
