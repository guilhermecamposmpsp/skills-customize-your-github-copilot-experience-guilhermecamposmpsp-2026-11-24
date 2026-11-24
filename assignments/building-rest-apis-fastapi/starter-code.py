from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Biblioteca de Livros")


class Book(BaseModel):
    title: str
    author: str
    year: int


# Armazenamento em memória: {id: Book}
books: dict[int, Book] = {}
next_id = 1


# Tarefa 1: crie a rota GET "/" que retorna uma mensagem de boas-vindas.

# Tarefa 2: crie a rota POST "/books" para cadastrar um livro.

# Tarefa 3: crie as rotas GET "/books" e GET "/books/{book_id}".

# Tarefa 4: crie as rotas PUT "/books/{book_id}" e DELETE "/books/{book_id}".
