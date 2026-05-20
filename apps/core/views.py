from django.shortcuts import render, redirect

from apps.collector.models import LeagueQuery
from apps.collector.forms import LeagueQueryForm

def index(request):
    if request.method == "POST":
        form = LeagueQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = LeagueQueryForm()

    return render(request, "core/index.html", {
        "form": form
    })
