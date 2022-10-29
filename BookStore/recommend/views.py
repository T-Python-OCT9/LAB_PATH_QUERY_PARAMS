from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from books import ClassBook.books 
from books.ClassBook import books


# Create your views here.
def printRandomItem(request : HttpRequest):
    randomItem = random.choice(books)
    return HttpResponse(randomItem)