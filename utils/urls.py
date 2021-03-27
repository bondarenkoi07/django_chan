from django.urls import path

from utils import views

urlpatterns = [
    path("search", views.search),
]
