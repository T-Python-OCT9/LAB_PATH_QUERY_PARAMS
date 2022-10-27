import imp
import random
from shutil import move
from select import select
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from . import bookclass as c



# Create your views here.


def view_books_all(request:HttpRequest):
    limit = int(request.GET.get('limit',3))
    all_books = "<br/>".join(c.books_list[:limit])

    return HttpRequest(all_books)

def view_books(request:HttpRequest,book_index):
    selected_book=c.books[book_index]
    return HttpResponse(f"The book :<br/>{selected_book.title}<br/><br/>The Auther:<br/>{selected_book.author}<br/><br/>Description:<br/>{selected_book.description}<br/><br/>Published in:<br/>{selected_book.publish_date}<br/><br/>")




