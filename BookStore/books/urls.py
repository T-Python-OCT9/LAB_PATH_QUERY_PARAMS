from django.urls import path
from . import views
from books.views import book

b2=book('english 106', 'english for proffisional ','omar','20/8/1999')

app_name = "books"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("books/list/", b2.view_books_all, name="view_books_all"),
    path("books/view/<book_id>", b2.getinfo , name="book_info")
]