
# API de Produtos

Esta é uma API simples para gerenciar produtos, construída com **FastAPI** e usando um arquivo JSON como banco de dados para armazenar informações sobre os produtos. A API permite criar, listar, atualizar e excluir produtos, além de filtrar os produtos disponíveis.

## Tecnologias Usadas

- **FastAPI**: Framework para criar APIs de alta performance com Python.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **Pydantic**: Para validação e serialização de dados.
- **JSON**: Usado como armazenamento para os dados dos produtos.

## Instalação

### Clonando o repositório

Para começar a usar a API, clone este repositório em seu ambiente local:

```bash
git clone https://github.com/diegotavares16/FastAPI_Loja.git
```

### Instalando dependências

1. Navegue até o diretório do projeto:

   ```bash
    cd nome-do-diretorio
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

## Executando a API

Para executar a API localmente, use o comando:

```bash
uvicorn app:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

Você também pode acessar a documentação interativa da API no seguinte endereço:

- [Documentação da API (Swagger UI)](http://127.0.0.1:8000/docs)

## Endpoints

A API oferece os seguintes endpoints para gerenciamento de produtos:

### 1. Listar todos os produtos

**GET** `/produtos`

Retorna todos os produtos no banco de dados.

### 2. Listar produtos disponíveis

**GET** `/produtos/disponiveis`

Retorna todos os produtos que estão disponíveis (`disponivel: true`).

### 3. Obter um produto pelo ID

**GET** `/produtos/{produto_id}`

Retorna um produto específico com base no seu `produto_id`.

### 4. Criar um novo produto

**POST** `/produtos`

Recebe um corpo de requisição com os dados de um novo produto e adiciona ao banco de dados.

**Exemplo de corpo da requisição**:

```json
{
  "nome": "Cadeira Gamer",
  "descricao": "Cadeira ergonômica para jogos",
  "preco": 799.99,
  "disponivel": true
}
```

### 5. Atualizar um produto existente

**PUT** `/produtos/{produto_id}`

Recebe um corpo de requisição com os dados atualizados de um produto.

**Exemplo de corpo da requisição**:

```json
{
  "nome": "Cadeira Gamer Pro",
  "descricao": "Cadeira ergonômica premium para jogos",
  "preco": 999.99,
  "disponivel": true
}
```

### 6. Deletar um produto

**DELETE** `/produtos/{produto_id}`

Deleta um produto pelo seu `produto_id`.

## Estrutura do Projeto

```
/meu-projeto
├── app.py            # Arquivo principal da aplicação FastAPI
├── produtos.py       # Modelos e lógica para manipulação de dados
├── produtos.json     # Arquivo JSON que armazena os dados dos produtos
├── requirements.txt  # Arquivo com as dependências do projeto
└── README.md         # Este arquivo
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.
