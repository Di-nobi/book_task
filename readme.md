## HOW TO RUN USING DOCKER
- run sudo docker compose up --build

## HOW TO RUN USING UVICORN (OPTIONAL)

- run uvicorn api.main:app --reload


### TO CREATE A BOOK USING CURL
- curl -X POST -H "Content-Type: application/json" -d '{"title": "TITLE", "author": "AUTHOR", "isbn": "342wwe34", "year": 0000}' http://localhost:8000/books

N/B - you can change the TITLE, AUTHOR, '342WWE34, 0000, to any data you want


### TO GET ALL BOOKS
- curl http://localhost:8000/books

### TO UPDATE A BOOK

-  curl -X PUT -F "title=New Title" -F "author=New Author" -F "isbn=dfjkedfjkwf" -F "year=2025" http://localhost:8000/books/{book_id}

n/b replace {book_id} with a specifc number of a book out of the books created and also the datas too if necessary

### GET A SEPCIFIC BOOK

- curl http://localhost:8000/books/{book_id}

### DELETE A BOOK

- curl -X DELETE http://localhost:8000/books/{book_id}
