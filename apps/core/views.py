from django.shortcuts import render, redirect

from apps.collector.forms import LeagueQueryForm

import json

from apps.web_scrapping.main_scrapper import scrape_laczynaspilka

test_list = [
       {
        "Pozycja": "1.",
        "Druzyna": "KKS LECH Poznań",
        "Mecze": "33",
        "Punkty": "59",
        "Wygrane": "16",
        "Remisy": "11",
        "Porazki": "6",
        "Gole_Zdobyte": "60",
        "Gole_Stracone": "43",
        "Bilans": "17"
    },
    {
        "Pozycja": "2.",
        "Druzyna": "GÓRNIK ZABRZE S.A.",
        "Mecze": "33",
        "Punkty": "53",
        "Wygrane": "15",
        "Remisy": "8",
        "Porazki": "10",
        "Gole_Zdobyte": "44",
        "Gole_Stracone": "36",
        "Bilans": "8"
    },
    {
        "Pozycja": "3.",
        "Druzyna": "Jagiellonia Białystok SSA",
        "Mecze": "33",
        "Punkty": "53",
        "Wygrane": "14",
        "Remisy": "11",
        "Porazki": "8",
        "Gole_Zdobyte": "55",
        "Gole_Stracone": "41",
        "Bilans": "14"
    },
    {
        "Pozycja": "4.",
        "Druzyna": "RKS RAKÓW CZĘSTOCHOWA S.A.",
        "Mecze": "33",
        "Punkty": "52",
        "Wygrane": "15",
        "Remisy": "7",
        "Porazki": "11",
        "Gole_Zdobyte": "48",
        "Gole_Stracone": "40",
        "Bilans": "8"
    },
]

def index(request):
    standing = None
    if request.method == "POST":
        form = LeagueQueryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["league_type"] = "Niższe ligi"

            standing = scrape_laczynaspilka(data["league_type"], wojewodztwo=data["province"], klasa=data["competition_class"], grupa=data["group"])

            print(data)
            print(standing)
    else:
        form = LeagueQueryForm()

    return render(request, "core/index.html", {
        "form": form,
        "standings": standing,
    })
