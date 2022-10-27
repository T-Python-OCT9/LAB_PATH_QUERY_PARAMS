from django.urls import path
from . import views

name_app = "Books"

urlpatterns = [
    path('view/', views.printBookList, name = "Books"),
    path('viewOne/<int:book_id>', views.printOneBook, name = "oneBook")
]