import random
from shutil import move
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from books.BooksClass import *
# Create your views here.
def random_recommend(request :HttpRequest):
    index=random.randrange(0,3)
    selected_book= books[index]
    return HttpResponse(f"Recommended Book for you <br/><br/>The book :<br/> {selected_book.title} <br/><br/> The Auther:<br/> {selected_book.author}<br/> <br/> Description:<br/>{selected_book.description}<br/><br/> Published in:<br/>{selected_book.publish_date}<br/><br/>")

