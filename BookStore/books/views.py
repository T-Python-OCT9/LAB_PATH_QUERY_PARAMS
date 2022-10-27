from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import book

# Create your views here.
booksList = []
booksList=book.books_list

def books_view(request : HttpRequest, books_index):
    selected_book = booksList[books_index]

    return HttpResponse(f" The book you selected is ----->  {selected_book}")
    
   
def view_all_books(request : HttpRequest):
    print(request.GET)
    limit = int(request.GET.get("limit",len(booksList[:])))
    all_books = "<br/>".join(booksList[:limit])
    
    return HttpResponse(all_books)

