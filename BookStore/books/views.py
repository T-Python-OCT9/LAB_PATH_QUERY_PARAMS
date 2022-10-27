from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import Book


# Create your views here.

Book_list = []
Book_list= Book.list_book
print (Book_list)


def all_list(request : HttpRequest):

    print(request.GET)
    #limit = int(request.GET.get("limit", len(Book_list[:])))
    #all_list = "<br/>".join(Book_list[:limit])
    all_list = Book_list
    

    return HttpResponse(f"this is all Books! : {all_list}")

def view_book(request : HttpRequest, book_index):
    
    selected_book = Book_list[book_index]

    return HttpResponse(f"book info: {selected_book}")