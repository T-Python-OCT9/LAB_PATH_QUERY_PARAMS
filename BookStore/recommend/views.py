from random import randint
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from books import views
# Create your views here.


def randombooks(request: HttpRequest):
    random = int(randint(0, len(views.books_list)-1))
    the_randon_book = views.books_list[random]

    return HttpResponse(the_randon_book)
 