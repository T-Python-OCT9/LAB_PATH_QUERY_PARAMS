from random import randint
from django.http import HttpRequest, HttpResponse
from books import models

# Create your views here.
def randomBook(request: HttpRequest):
    book_id: int = randint(0, len(models.books_list) - 1)
    book = f'<h2>{models.books_list[book_id].title}</h2><span>Author: {models.books_list[book_id].author} | Published: {models.books_list[book_id].publish_date}</span><br /><p>{models.books_list[book_id].description}</p> <br />'
    return HttpResponse(book)