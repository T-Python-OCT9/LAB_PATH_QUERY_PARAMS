
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
from random import random

# Create your views here.

BooksList = ["city that never sleeps","the art of giving up","do not give up"]

def RandomBook(request: HttpRequest):

    random_book = (request.GET.get("random_book"))

    return HttpResponse(f'this random book {random_book.random.choice(BooksList)} ')


       
     
        

        
            
       
                    
   


