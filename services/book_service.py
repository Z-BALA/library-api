from repositories.book_repository import *

def formatar_book(book):
    book["_id"] = str(book["_id"])
    return book

def create_book_service(book):
    result = create_book(book.model_dump())
    return {"mensagem": "Livro cadastrado", "id": str(result.inserted_id)}

def get_all_books_service():
    books = get_all_books()
    return [formatar_book(b) for b in books]

def get_book_by_id_service(book_id):
    try:
        book = get_book_by_id(book_id)
    except Exception:
        return {"erro": "ID invalido"}
    if not book:
        return {"erro": "Livro nao encontrado"}
    return formatar_book(book)

def update_book_service(book_id, book):
    try:
        result = update_book(book_id, book.model_dump())
    except Exception:
        return {"erro": "ID invalido"}
    if result.matched_count == 0:
        return {"erro": "Livro nao encontrado"}
    return {"mensagem": "Livro atualizado"}

def delete_book_service(book_id):
    try:
        result = delete_book(book_id)
    except Exception:
        return {"erro": "ID invalido"}
    if result.deleted_count == 0:
        return {"erro": "Livro nao encontrado"}
    return {"mensagem": "Livro deletado"}
