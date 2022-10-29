from django.urls import path
from . import views
from . import ClassBook

name_app = "Books"

urlpatterns = [
    path('view/<int:book_id>', 'views.printBookList', name = "Books"),
    path('view/', views.printBookList, name = "Books"),
    path('viewOne/<int:book_id>', views.printOneBook, name = "oneBook")
]