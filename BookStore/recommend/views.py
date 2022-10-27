import random
from django.shortcuts import render
from shutil import move
from django.http import HttpRequest, HttpResponse
from books.views import book

# Create your views here.

x=book.books_list

def view_movie(request : HttpRequest):
    
    rand_idx = random.randrange(len(x))
    random_num = x[rand_idx]

    return HttpResponse(f"the recommended book is: {random_num}")


