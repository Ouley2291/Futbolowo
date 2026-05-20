from django.shortcuts import render, redirect

from apps.collector.forms import LeagueQueryForm

def index(request):
    if request.method == "POST":
        form = LeagueQueryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["league_type"] = "Niższe ligi"

            print(data)

            return redirect("core:index")
    else:
        form = LeagueQueryForm()

    return render(request, "core/index.html", {
        "form": form
    })
