from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("list/", views.list_all_books, name = "list_all_books"),
    path("view/<int:book_id>/", views.view_book, name="view_book"),
    path("home/", views.home, name="home")
]