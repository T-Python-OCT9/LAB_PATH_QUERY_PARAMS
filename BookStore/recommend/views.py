from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from random import randint
from books import views

# Create your views here.

def randomBooks(request : HttpRequest):

    randomizer = int( randint (0,len(views.booksList)-1))
    random_book = views.booksList[randomizer]
    
    return HttpResponse(random_book)

