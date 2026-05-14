from django.shortcuts import render
from .models import Player, sort_bys_position

def team_stats(request):
    players = Player.objects.all().order_by("number")
    players = sort_bys_position(players)

    return render(request, 'players/team_stats.html', {
        "players": players,
    })
