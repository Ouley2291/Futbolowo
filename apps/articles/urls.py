from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("/add", views.add, name="add"),
    path("/view/<int:id>", views.add, name="view"),
]