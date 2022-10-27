from django.urls import path
from . import views
from books import classes as c

app_name = "recommend"
urlpatterns = [
    path(f"random/", views.random_recommend, name = "Recommend book"),
    ]