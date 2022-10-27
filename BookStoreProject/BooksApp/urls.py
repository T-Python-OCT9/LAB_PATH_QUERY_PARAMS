from django.urls import path
from . import views

app_name = 'BooksApp'

urlpatterns = [
    path('list/', views.ListAllBooks, name='ListAllBooks'),
    path('view/<int:book_id>/', views.GetBook, name='GetBook'),
]