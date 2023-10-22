from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Sport"},
    {"title": "Title Three", "author": "Author Three", "category": "Programming"},
    {"title": "Title Four", "author": "Author Four", "category": "Art"},
    {"title": "Title Five", "author": "Author Five", "category": "Design"},
    {"title": "Title Six", "author": "Author Six", "category": "Science"},
]


@app.get("/")
async def first_api():
    return BOOKS


@app.get("/books/{book_title}")
async def read_all_books(book_title: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get('title').casefold() == book_title.casefold() and
                book.get("category").casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/my-books/{author}")
async def my_books(author: str, title: str):
    books_return_list = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold() == author.casefold() \
                and BOOKS[i].get("title").casefold() == title.casefold():
            books_return_list.append(BOOKS[i])
