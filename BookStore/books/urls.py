from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("view/<int:book_index>/", views.view_book, name = "view_book"),
    path("books/list", views.view_book_all, name="view_book_all")
]