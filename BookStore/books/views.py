from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .bookClass import books


    


def printBookList(request:HttpRequest):
    books_endpoint = int(request.GET.get("limit"))
    slice_books = books[:books_endpoint]
    return HttpResponse(slice_books)

def printOneBook(request:HttpRequest, book_id):
    oneBook = books[book_id]
    return HttpResponse(oneBook)

