from django.urls import path
from . import views


app_name = "Books"


urlpatterns = [
    path("list/", views.books_list, name="books"),
    path("view/<int:books_index>", views.books_list, name="books_view" )
]