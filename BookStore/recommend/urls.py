from django.urls import path
from . import views

app_name = "recommend"

urlpatterns = [ 
     path("recommend/random/", views.RandomBook, name = "random book"),
     
  ]