from fastapi import FastAPI, Form
from models.books import Books
from database.db import storage


my_app = FastAPI()
my_storage = storage()
@my_app.get('/books')
async def all_books():
    """Returns the list of all books"""
    list_books = []
    for count in my_storage.all():
        list_books.append(count)
    return {'Books': list_books}

@my_app.get('/books/{book_id}')
async def get_book(book_id: int):
    """Gets a single book"""
    book = my_storage.get_a_book_by_id(book_id)
    if not book:
        return f'This book dosent exist'
    return {'book': book}

@my_app.post('/books')
async def create_book(books: dict):
    try:
        my_storage.add_book(**books)
        return {'Book created successfully'}
    except Exception as er:
        return f'error occured at {er}'

@my_app.put('/books/{book_id}')
async def update_book(book_id: int, title: str=Form(...), author:str=Form(...), isbn: str=Form(...), year: int=Form(...)):
    """Updates the book"""
    get_book = my_storage.get_a_book_by_id(book_id)
    if not get_book:
        return None
    get_book.title = title
    get_book.author = author
    get_book.isbn = isbn
    get_book.year = year
    return {'New created book': get_book}
@my_app.delete('/books/{book_id}')
async def del_book(book_id):
    """Deletes a book from the database"""
    get_book = my_storage.get_a_book_by_id(book_id)
    if not get_book:
        return None
    my_storage.remove(get_book)
    return {'Book deleted': {}}