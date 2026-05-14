from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'players'

urlpatterns = [
    path("/team_stats", views.team_stats, name="team_stats"),
    path("/player_stats/<int:id>", views.player_stats, name="player_stats")
]