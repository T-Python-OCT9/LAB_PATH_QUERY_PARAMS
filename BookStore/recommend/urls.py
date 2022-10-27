from django.urls import path
from . import views

app_name = "Recommend"

urlpatterns = [
    path("random/", views.aandom, name="recommend"),
    
]