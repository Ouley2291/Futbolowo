from django.shortcuts import render, get_object_or_404
from .models import Player, sort_by_position

def team_stats(request):
    players = Player.objects.all().order_by("number")
    players = sort_by_position(players)

    return render(request, 'players/team_stats.html', {
        "players": players,
    })


def player_stats(request, id):
    player = get_object_or_404(Player, pk=id)

    return render(request, 'players/player.html', {
        "player": player,
    })
