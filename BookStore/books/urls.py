from django.urls import path
from . import views


app_name = "Books"


urlpatterns = [
    path("list/", views.view_all_books, name="view_all_books"),
    path("view/<int:books_index>", views.books_view, name="books_view" )
]
