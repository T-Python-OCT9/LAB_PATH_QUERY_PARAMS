from django.shortcuts import render
from random import randint
from django.http import HttpRequest, HttpResponse
from BooksApp import views as v

# Create your views here.
def RandomBook(request: HttpRequest):
    book_id = randint(0, len(v.AllBooks) - 1)
    return HttpResponse(v.AllBooks[book_id])