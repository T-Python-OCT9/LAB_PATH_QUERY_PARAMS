from django.urls import path
from . import views

app_name = "recommend"

urlpatterns = [
    path("recommend/random/", views.view_movie, name="view_movies_all")
]