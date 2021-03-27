from django.urls import path, re_path

from utils import views

urlpatterns = [
    path("search", views.search),
]
