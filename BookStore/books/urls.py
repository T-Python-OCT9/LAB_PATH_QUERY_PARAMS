from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("view/<int:book_index>/", views.view_books, name = "view book"),
    path("list/", views.view_books_all, name="view_books_all")
]