from django.http import HttpRequest, HttpResponse
from . import models


# Create your views here.
def booksList(request: HttpRequest):
    limit = request.GET.get('limit')
    books = list()
    if limit and (int(limit) < len(models.books_list)):
        for i in range(0, int(limit)):
            books.append(f'<h2>{models.books_list[i].title}</h2><span>Author: {models.books_list[i].author} | Published: {models.books_list[i].publish_date}</span><br /><p>{models.books_list[i].description}</p> <br />')
        books = ' '.join(books)
    else:
        for i in range(0, len(models.books_list)):
            books.append(f'<h2>{models.books_list[i].title}</h2><span>Author: {models.books_list[i].author} | Published: {models.books_list[i].publish_date}</span><br /><p>{models.books_list[i].description}</p> <br />')
        books = ' '.join(books)
    return HttpResponse(books)

def bookID(request : HttpRequest, book_id: str):
    book_id: int = int(book_id) - 1
    book = f'<h2>{models.books_list[book_id].title}</h2><span>Author: {models.books_list[book_id].author} | Published: {models.books_list[book_id].publish_date}</span><br /><p>{models.books_list[book_id].description}</p> <br />'
    return HttpResponse(book)