 
from django.urls import path
from . import views

app_name = "books"

urlpatterns = [ 
     path("books/", views.books, name = "books list"),
     path("books/<Bindex>/", views.SelectBook, name = "one book")
  ]