from fastapi import FastAPI, Form
from models.books import Books
from database.db import storage


my_app = FastAPI()
my_storage = storage()
@my_app.get('/books', tags=['BOOKS'])
async def all_books():
    """
    Retrieves the list of all the books

    Returns:
        A dictionary containing all the books
    """
    list_books = []
    for count in my_storage.all():
        list_books.append(count)
    return {'Books': list_books}

@my_app.get('/books/{book_id}', tags=['BOOKS'])
async def get_book(book_id: int):
    """
    Retrieves a book from the database

    Args:
        book_id (int): The book to get from the database

    Returns:
        A dictionary containing  the book
    """
    book = my_storage.get_a_book_by_id(book_id)
    if not book:
        return f'This book dosent exist'
    return {'book': book}

@my_app.post('/books', tags=['BOOKS'])
async def create_book(books: dict):
    """
    Creates a new book and adds it to the database

    Returns:
        A dictionary containing  the new book
    """
    try:
        my_storage.add_book(**books)
        return {'message': 'Book created successfully'}
    except Exception as er:
        return f'error occured at {er}'

@my_app.put('/books/{book_id}', tags=['BOOKS'])
async def update_book(book_id: int, title: str=Form(...), author:str=Form(...), isbn: str=Form(...), year: int=Form(...)):
    """
    Updates a book in the database

    Args:
        book_id (int): The book to verify and get from the database

    Returns:
        A dictionary containing  the new information of the book
    """
    get_book = my_storage.get_a_book_by_id(book_id)
    if not get_book:
        return None
    get_book.title = title
    get_book.author = author
    get_book.isbn = isbn
    get_book.year = year
    return {'New updated book': get_book}
@my_app.delete('/books/{book_id}', tags=['BOOKS'])
async def del_book(book_id):
    """
    Deletes a book from the database

    Args:
        book_id (int): The book to get from the database

    Returns:
        A successfully deleted message
    """
    get_book = my_storage.get_a_book_by_id(book_id)
    if not get_book:
        return None
    my_storage.remove(get_book)
    return {'message': 'Book deleted successfully'}