from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import random
from BooksInfo import *

# Create your views here.
def recommend(request:HttpRequest):
    random_books = random.randrange(0,4)
    random_Book = Book.book_info[random_books]
    
    return HttpResponse(random_Book)