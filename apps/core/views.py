from django.shortcuts import render, redirect
from apps.collector.forms import LeagueQueryForm, GROUP_CHOICES
import json
from apps.web_scrapping.main_scrapper import scrape_laczynaspilka
from apps.Leagues.models import League, LeagueStanding

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

            league, created = League.objects.get_or_create(competition_class=data["competition_class"], province=data["province"], group=data["group"], season=data["season"])

            if created:
                standing = scrape_laczynaspilka(data["league_type"], wojewodztwo=data["province"], klasa=data["competition_class"], grupa=data["group"])
                for pos in standing:
                    new_team = LeagueStanding.objects.create(
                        league = league,
                        position = pos["Pozycja"],
                        team = pos["Druzyna"],
                        match_count = int(pos["Mecze"]),
                        points = int(pos["Punkty"]),
                        win_count = int(pos["Wygrane"]),
                        draw_count = int(pos["Remisy"]),
                        loose_count = int(pos["Porazki"]),
                        goals_scored = int(pos["Gole_Zdobyte"]),
                        goals_conceded = int(pos["Gole_Stracone"]),
                        goals_balance = int(pos["Bilans"])
                    )
            standing = league.positions.all().order_by("position")

            #print(data)
            #print(standing)
    else:
        form = LeagueQueryForm()

    return render(request, "core/index.html", {
        "form": form,
        "standings": standing,
        "groups": json.dumps(GROUP_CHOICES, ensure_ascii=False)
    })
