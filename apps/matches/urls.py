from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'matches'

urlpatterns = [
    path("/highlights_list", views.highlights_list, name="highlights_list"),
    path("/upload_highlight", views.upload_highlight, name="upload_highlight")
]