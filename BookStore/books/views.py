from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
# Create your views here.

class Books:
    book_list : list = []
    def __init__(self,name: str,discription: str,author: str,publish_date: str):
        self.name = name
        self.discription = discription
        self.author = author 
        self.publish_date= publish_date
        
        Books.book_list.append([f'The Book Name Is: {name}',f'Discription: {discription}',f'Publisher: {publish_date}',f'Author: {author}'])


book1 = Books('clean code','book to write code better.','1/2/2000','Robert C. Martin')
book1 = Books('python','learn python','1/2/2026','aqeel')
book1 = Books('jsva','learn java','1/2/2000','Robert C. Martin')

def all_books(request : HttpRequest):
    # limit = int(request.GET.get('limit'))
    string = ''
    for index,book_lists in enumerate(Books.book_list):
        for book_list in book_lists:
            book = '<br>'.join(book_lists)
        string = string +" "+ book 
    return HttpResponse(string)
    
   

def search_for_book(request : HttpRequest, book_name):
    string = ''
    name = f'The Book Name Is: {book_name}'
    for book_lists in Books.book_list:
        for book_list in book_lists:
            if book_list == name:
                for book_attributes in book_lists:
                    book = ''.join(book_attributes)
                    string = string +" "+ book 
    return HttpResponse(string)

def random_book(request : HttpRequest):
    num = random.randrange(0,len(Books.book_list))
    string = ''
    for index,book_lists in enumerate(Books.book_list):
        if index == num:
            for book_list in book_lists:
                book = '<br>'.join(book_lists)
            string = string +" "+ book 
    return HttpResponse(string)


def home(request: HttpRequest):
    msg = "Welcome"
    return HttpResponse(msg)


