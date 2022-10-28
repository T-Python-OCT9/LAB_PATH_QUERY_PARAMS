from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from .book import Books

# Create your views here.

book1 = Books('clean code','book to write code better.','1/2/2000','Robert C. Martin')
book2 = Books('python','learn python','1/2/2026','aqeel')
book3 = Books('jsva','learn java','1/2/2000','Robert C. Martin')

book_list = [book1, book2, book3]

def all_books(request:HttpRequest):

    limit = int(request.GET.get("limit", 5))
    content = ""

    for book in book_list[:limit]:
        content += f"{book.describe()} <br/>"

    return HttpResponse(content)


def view_book(request: HttpRequest, book_id):
    book = book_list[book_id]
    return HttpResponse(book.describe())


def home(request: HttpRequest):
    msg = "Welcome"
    return HttpResponse(msg)


