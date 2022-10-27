from django.urls import path
from . import views

app_name = 'RecommendApp'

urlpatterns = [
    path('random/', views.RandomBook, name='randomBook')
]