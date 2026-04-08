# Library API

API de cadastro de livros feita com FastAPI, MongoDB e Docker.

## Tecnologias usadas

- FastAPI
- MongoDB
- Docker

## Como rodar

entre na pasta do projeto

```bash
docker-compose up --build
```

Acesse a documentação em: http://localhost:8000/docs

## Endpoints

- GET /books - lista todos os livros
- POST /books - cadastra um livro
- GET /books/{id} - busca livro por id
- PUT /books/{id} - atualiza um livro
- DELETE /books/{id} - deleta um livro

## Schema

```json
{
  "titulo": "string",
  "autor": "string",
  "ano": 0,
  "genero": "string"
}
```
👍✌️
