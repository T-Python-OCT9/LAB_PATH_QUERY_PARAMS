from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 

# Create your views here.

BooksList = ["city that never sleeps","the art of giving up","do not give up"]

def books(request: HttpRequest):

    limit = int(request.GET.get("limit"))
    all_list = "<br/>".join(BooksList[limit]) 
    return HttpResponse(all_list)

def SelectBook(request:HttpRequest, Bindex):
    one_book = BooksList[Bindex]
    return HttpResponse(one_book)

