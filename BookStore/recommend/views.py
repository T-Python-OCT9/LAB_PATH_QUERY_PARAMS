from select import select
from textwrap import indent
from django.shortcuts import render
import random
from django.http import HttpRequest,HttpResponse
from books.bookclass import*


# Create your views here.

def random_recommend(request:HttpRequest):
    index=random.randrange(0,2)
    selected_book=books[index]
    return HttpResponse(f"Recommended Book for you <br/>{selected_book.title}<br/><br/>The Auther:<br/>{selected_book.author}<br/><br/>Description:<br/>{selected_book.description}<br/><br/>Published in:<br/>{selected_book.publish_date}<br/><br/>")
