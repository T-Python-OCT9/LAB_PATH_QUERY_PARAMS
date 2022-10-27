from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


class Book():
    def __init__(self, title, description, author, publish_date) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date

    def bookinfo(self):
        return f"\ntitle : {self.title}\n description: {self.description}\n author:{self.author}\n publish_date:{self.publish_date}"


book1 = Book("Clean Code", "Clean Code", "robert cecil martin", "01-09-2008")
book2 = Book("Design Pattrns", "Design Pattrns",
             "john matthew vlissides", "24-11-2005")
book3 = Book("The Mythical Man-month", "The Mythical Man-month",
             "frederick p brooks", "00-90-1995")
book4 = Book("Code Complete", "Code Complete", "steve mcConnell", "11-00-1993")

book_one = book1.bookinfo()
book_two = book2.bookinfo()
book_three = book3.bookinfo()
book_four = book4.bookinfo()
books_list = [book_one, book_two, book_three, book_four]

'''
def home(request: HttpRequest):
    msg = "Welcome to my new Home"
    return HttpResponse(msg)'''


def view_books_all(request: HttpRequest):

    limit = int(request.GET.get("limit", 4))
    all_books = "<br/>".join(books_list[:limit])

    return HttpResponse(all_books)


def view_books(request: HttpRequest, books_index):

    selected_book = books_list[books_index]

    return HttpResponse(f"the book is: {selected_book}")
