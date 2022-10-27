from django.urls import path
from.import views
from.import bookclass

name_app = 'Books'
urlpatterns=[
    path('view/<int:book_id>' , 'views.printBookList' , name='Books')
]