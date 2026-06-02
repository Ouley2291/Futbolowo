from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("/add", views.add, name="add"),
    path("/view/<int:id>", views.article_view, name="view"),
    path("/list", views.article_list, name="list"),
    path("/edit/<int:id>", views.edit, name="edit"),
]