from django.shortcuts import render
from .models import Player

def team_stats(request):
    players = Player.objects.all()

    return render(request, 'players/team_stats.html', {
        "players": players,
    })
