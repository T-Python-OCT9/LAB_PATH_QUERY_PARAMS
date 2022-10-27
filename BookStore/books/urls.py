from django.urls import path
from . import views

app_name = 'Books'

urlpatterns = [
    path("", views.home, name="home"),
    path("book/list", views.all_books, name="books"),
    path('book/view/<book_name>',views.search_for_book, name='searsh'),
    path('recommend/random/', views.random_book, name= 'random')

]