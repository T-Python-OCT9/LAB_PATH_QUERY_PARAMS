from django.urls import path
from . import views

app_name = "book"

urlpatterns=[

path("list/<int:b_index>" ,views.all_books, name = "all book")

]