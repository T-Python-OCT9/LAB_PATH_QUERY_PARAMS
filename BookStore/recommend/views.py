from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from books import views
# Create your views here.

def random_book(request: HttpRequest):

    random_book = random.choice(views.book_list)

    return HttpResponse(random_book.describe())
