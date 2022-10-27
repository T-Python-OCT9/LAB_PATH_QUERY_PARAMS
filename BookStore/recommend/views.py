from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
from books import book_list
# Create your views here.


def Random_Book (request:HttpRequest):
    random_book = random.choice(book_list)

    return HttpResponse(random_book)