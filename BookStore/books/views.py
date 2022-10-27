from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from booksclass import *


book1 = book ("harry potter","fantasy novel","J. K. Rowling","1997")
book2 = book ("The Witcher","fantasy novel","Andrzej Sapkowski","1986")
book3 = book ("Game of Thrones","fantasy novel","George RR Martin","1996")
book4 = book ("Lord of the Rings","fantasy Novel","J. R. R. Tolkien","1968")

bookone =book1.printBookDetails()
booktwo =book2.printBookDetails()
bookthree =book3.printBookDetails()
bookfour =book4.printBookDetails()


book_list =  [bookone,booktwo,bookthree,bookfour]

def view_book_all(request:HttpRequest):
    limit = int(request.GET.get("limit"))
    all_books = "<br/>".join(book_list[:limit])

    return HttpResponse (all_books)

def view_book (request: HttpRequest,book_index):

    selected_book = book_list[book_index]    
    
    return HttpResponse (f"the book is : {selected_book}")

def home(request: HttpRequest):
    msg = "Welcome to my new Home"
    return HttpResponse(msg)

# Create your views here.
