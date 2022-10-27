from django.urls import path
from . import views

app_name = "BookStore"

urlpatterns = [

path("recommend/random/", views.recommend, name="recommend"), 
]
