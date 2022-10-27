from django.shortcuts import render
from shutil import move
from django.http import HttpRequest, HttpResponse

# Create your views here.
class book:

    books_list=[]
    

    def __init__(self , title, description, author,publish_date ) -> None:
        self.title=title
        self.description=description
        self.author=author
        self.publish_date=publish_date
        self.books_list.append(self.title)
        

    def view_books_all(self, request : HttpRequest):
        limit = int(request.GET.get("limit", 10))
        all_books = "<br/>".join(self.books_list[:limit])
        return HttpResponse(all_books)
    
    def getinfo(self, book_id):
        return f"\ntitle : {self.title}\n description: {self.description}\n author:{self.author}\n publish_date:{self.publish_date}"
    


        


def home(request: HttpRequest):
    msg = "Welcome to my new Home"
    return HttpResponse(msg)

b1=book('math101','introduction to math','ahmed','9/11/2000')
b2=book('english 101', 'english for biggners','omar','8/8/1999')
