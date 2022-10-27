from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .booksclass import book
from datetime import date

book1 = book ("harry potter","fantasy novel","J. K. Rowling",date(1998,2,10))
book2 = book ("The Witcher","fantasy novel","Andrzej Sapkowski",date(1899,5,10))
book3 = book ("Game of Thrones","fantasy novel","George RR Martin",date(1996,2,10))
book4 = book ("Lord of the Rings","fantasy Novel","J. R. R. Tolkien",date(1994,3,10))



book_list =  [book1,book2,book3,book4]


def list_all_books(request:HttpRequest):

    limit = int(request.GET.get("limit", 5))

    output = ""

    for book in book_list[:limit]:
        output += f"{book.describe()} <br/>"
    
    return HttpResponse(output)


def view_book(request: HttpRequest, book_id):
    book = book_list[book_id]
    return HttpResponse(book.describe())

def home(request: HttpRequest):
    msg = "Welcome to my new Home"
    return HttpResponse(msg)

# Create your views here.
