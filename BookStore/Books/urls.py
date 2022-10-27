from django.urls import path
from . import views


app_name = "Books"

urlpatterns =[
    path("list/",'views.Show_books',name="ShowBooks"),
    path("view/<int:BookID>",'views.show_one_book',name="oneBook"),
]