from django.shortcuts import render
from shutil import move
from django.http import HttpRequest, HttpResponse
from Books import BooksInfo 


BooksList=[]
BooksList=BooksInfo.Books_list



def Show_books(request: HttpRequest):
    limit = int(request.GET. get("limit"))
    all_books = "<br/>".join(BooksList[:limit])
    return HttpResponse(all_books)

def show_one_book(request: HttpRequest,BookID):
    oneBook=BooksList[BookID] 
    return HttpResponse(oneBook)
