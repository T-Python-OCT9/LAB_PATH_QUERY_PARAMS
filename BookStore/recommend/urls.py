from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
   path('recommend/random/', views.random_book, name= 'random')
]



