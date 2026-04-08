from fastapi import APIRouter
from schemas.book_schema import Book
from services.book_service import *

router = APIRouter()

#GET - todos os livros
@router.get("/books")
def listar_books():
    return get_all_books_service()

#POST - cadastrar livro
@router.post("/books")
def cadastrar_book(book: Book):
    return create_book_service(book)

#GET - buscar livro por id
@router.get("/books/{book_id}")
def buscar_book(book_id: str):
    return get_book_by_id_service(book_id)

#PUT - atualizar livro
@router.put("/books/{book_id}")
def atualizar_book(book_id: str, book: Book):
    return update_book_service(book_id, book)

#DELETE - deletar livro
@router.delete("/books/{book_id}")
def deletar_book(book_id: str):
    return delete_book_service(book_id)
