from random import randint
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from books import views

# Create your views here.



def aandom(request : HttpRequest):

    random= views.Book_list
    rand = int(randint (1,4))
    recomand= random[rand]

    return HttpResponse(recomand)


