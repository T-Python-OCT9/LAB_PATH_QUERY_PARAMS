from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

#Note : Create a calss to represent a book, the book should have the follwoing attributes :

class Books():
    def __init__(self, title : str ,description : str , author : str , publish_date : str) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date
    def display(self):
        return f"<br> <b>Title:</b> {self.title} <br> <b> Description: </b>  {self.description} <br> <b> Author: </b> {self.author} <br> <b> Published Date: </b> {self.publish_date} <br> <hr>"

AllBooks = [
    Books("All of Programming", " teach students to deeply understand how the code works by teaching students how to execute the code by hand","Andrew Hilton","2019").display(),
    Books("Introduction To Algorithms", "Introduction to Algorithms combines rigor and comprehensiveness. The book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers.","Thomas H Cormen","2001").display(),
    Books("Computer Programming for Beginners: A Step-by-step Guide", "This book aims to capture the fundamentals of computer programming without tying the topic to any specific programming language. To the best of the authors' knowledge there is no such book in the market.","Murali Chemuturi ","2018").display(),
]
# Create your views here.


def GetBook(request : HttpRequest, book_id):
    return HttpResponse(AllBooks[book_id])


def ListAllBooks(request : HttpRequest):
    return HttpResponse(AllBooks[:int(request.GET.get("limit",len(AllBooks[:])))])



