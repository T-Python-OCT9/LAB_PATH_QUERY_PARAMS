from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from Books import *
from random import randint
from Books import views 

# Create your views here.

def randomBook(request:HttpRequest):
    randoms = int( randint (0,len(views.booksList)-1))
    random_book = views.BooksList[randoms]

    return HttpResponse(random_book)