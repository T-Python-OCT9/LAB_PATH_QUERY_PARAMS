from django.urls import path
from . import views

app_name = "BookStore"

urlpatterns = [

path("list/", views.book_List_View, name="book_List_View"), 
path("view/<int:books_Index>/" , views.select_Books , name="select_Books")
]

