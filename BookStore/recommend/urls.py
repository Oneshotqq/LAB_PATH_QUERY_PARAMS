from django.urls import path
from . import views

app_name="recommend"


urlpatterns = [
    path("random/", views.Random_Book, name="random_book"),
]