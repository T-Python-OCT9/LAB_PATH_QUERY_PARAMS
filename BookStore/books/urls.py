from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("view/<int:books_index>/", views.view_books, name="view books"),
    path("view/all/", views.view_books_all, name="view_books_all"),
]
