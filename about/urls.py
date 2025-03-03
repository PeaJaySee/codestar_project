from . import views
from django.urls import path

url_patterns = [
    path("", views.about_me, name="about"),
]