# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI: definir rotas, validar dados com modelos Pydantic e implementar as operações de CRUD (criar, ler, atualizar e remover) sobre uma coleção de livros armazenada em memória.

Ao final, sua API deve responder às requisições HTTP corretas e poder ser testada pela documentação interativa em `/docs`.

## 📝 Tarefas

### 🛠️ Primeira Rota

#### Descrição
Crie a aplicação FastAPI e uma rota que responda a requisições `GET` na raiz do site. Esse é o primeiro passo para entender como o FastAPI associa funções Python a endereços HTTP.

#### Requisitos
O programa completo deve:

- Criar a rota `GET /` com a função `read_root()`
- Retornar um dicionário com a chave `message` e uma mensagem de boas-vindas
- Executar o servidor com `uvicorn main:app --reload` e acessar `http://127.0.0.1:8000/` no navegador


### 🛠️ Cadastrar Livros

#### Descrição
Crie um modelo de dados `Book` com `Pydantic` e uma rota `POST /books` que cadastre um novo livro. A API deve validar os dados recebidos e atribuir um `id` único a cada livro.

#### Requisitos
O programa completo deve:

- Usar o modelo `Book` (já definido no starter code) para validar o corpo da requisição
- Criar a rota `POST /books` que salve o livro no dicionário `books` com um novo `id`
- Incrementar `next_id` a cada cadastro
- Retornar o livro cadastrado com o `id` e o status HTTP `201 Created`
- Testar o cadastro pela interface `/docs`, enviando um livro com `year` em formato inválido e verificando o erro `422`


### 🛠️ Consultar Livros

#### Descrição
Implemente as rotas de leitura: uma para listar todos os livros e outra para buscar um livro pelo `id`. Quando o livro não existir, a API deve responder com `404 Not Found`.

#### Requisitos
O programa completo deve:

- Criar a rota `GET /books` que retorne a lista de todos os livros
- Criar a rota `GET /books/{book_id}` que retorne um livro específico
- Usar `HTTPException` com status `404` quando o `book_id` não existir
- Aceitar o parâmetro de consulta opcional `author` em `GET /books` e retornar apenas os livros desse autor (ex.: `/books?author=Machado de Assis`)


### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete o CRUD implementando a atualização e a remoção de livros. Este é o desafio final: ele exige combinar rotas com parâmetros de caminho, validação, códigos de status e tratamento de erros.

#### Requisitos
O programa completo deve:

- Criar a rota `PUT /books/{book_id}` que substitua os dados de um livro existente
- Criar a rota `DELETE /books/{book_id}` que remova o livro e retorne o status `204 No Content`
- Retornar `404 Not Found` nas duas rotas quando o livro não existir
- Verificar, pela interface `/docs`, que todas as rotas aparecem documentadas automaticamente
