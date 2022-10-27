from urllib.request import Request
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.
class book :

    def __init__(self,title: str , description, author ,publish_date ) -> None:
    
        self.title = title
        self.description=description
        self.author = author
        self.publish_date = publish_date


book1 = book ("Harry Potter", "fantzi" , "J. K. Rowling" ,"26 June 1997")
book2 = book ("War and Peace" , "war" , "Leo Tolstoy" , " 1899")
book3 = book ("Madame Bovary" , "hilthe" , "Gustave Flaubert" , "1856")

books_list = [book1, book2,book3]
#print(book1 + book2 +book3)
 


def all_books(request : HttpRequest):
    print(request.GET)
    limit = int(request.GET.get("limit",len(books_list[:])))
    all_books = "<br/>".join(books_list[:limit])

    return HttpResponse(all_books)
