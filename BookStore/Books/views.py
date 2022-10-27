from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from  BooksInfo import *


book_List = [book1, book2.book_info , book3.book_info , book4.book_info , book5.book_info]

def book_List_View(request:HttpRequest):
    
    limit = int(request.GET.get("limit" ))
    all_Books = "<br/>".join(book_List[:limit])
    return HttpResponse(all_Books)

def select_Books(request:HttpRequest , books_Index):
    select_books = book_List[books_Index]
    return HttpResponse(f"Book : {select_books}")
