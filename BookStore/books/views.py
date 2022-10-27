from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

book_list=["Harry Potter","To Kill a Mockingbird" , "The Book Thief "] 

def all_books(request: HttpRequest , b_index ):

   selectB = book_list[b_index]
   return HttpResponse(f"the book is :{selectB}")