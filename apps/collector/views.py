from django.shortcuts import render
from apps.matches.models import League, StandingEntry
import json

def receive_standings(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return render(request, "matches/standings.html", {
            
        })
    
