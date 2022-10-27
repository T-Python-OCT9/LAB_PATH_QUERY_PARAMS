from django.urls import path
from . import views

name_app = "Random"

urlpatterns = [
    path('random/', 'views.printRandomItem', name = "Random"),
]