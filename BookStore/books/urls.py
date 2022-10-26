from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('list/', views.booksList, name='books_list'),
    path('view/<book_id>/', views.bookID, name='books_list'),
]