from django.urls import path
from . import views

app_name = "Books"

urlpatterns = [
    path("list/", views.all_list, name="view all books"),
    path("view/<int:book_index>/", views.view_book, name = "Book Id")
]