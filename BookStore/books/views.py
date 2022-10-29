
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ClassBook import *
from .ClassBook import books


bk1 = BookClass("Moonlight Cove", "Family and friends mean everything", "Sherryl Woods", "2017")
bk2 = BookClass("Moonlight", "Family is everything", "Sherryl Woofs", "2013")
bk3 = BookClass("Moonlight Cove", "friends mean everything", "Sherryl Wolds", "2016")

book1 = bk1.printBookDetails()
book2 = bk2.printBookDetails()
book3 = bk3.printBookDetails()


books = [book1, book2, book3]

def printBookList(request:HttpRequest):
    books_endpoint = int(request.GET.get("limit"))
    slice_books = books[:books_endpoint]
    return HttpResponse(slice_books)
def printOneBook(request:HttpRequest, book_id):
    oneBook = books[book_id]
    return HttpResponse(oneBook)