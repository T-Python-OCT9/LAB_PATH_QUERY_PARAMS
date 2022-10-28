from django.urls import path
from . import views

app_name = 'Books'

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.all_books, name="books"),
    path('view/<int:book_id>',views.view_book, name='searsh'),
    
]