from django import forms
from .models import LeagueQuery

class LeagueQueryForm(forms.Form):    
    SEASON_CHOICES = [
        ("2025/2026", "2025/2026"),
        ("2024/2025", "2024/2025"),
        ("2023/2024", "2023/2024"),
    ]

    PROVINCE_CHOICES = [
        ("dolnośląskie", "Dolnośląskie"),
        ("kujawsko-pomorskie", "Kujawsko-Pomorskie"),
        ("lubelskie", "Lubelskie"),
        ("wielkopolskie", "Wielkopolskie"),
    ]

    COMPETITION_CLASS_CHOICES = [
        ("Czwarta liga", "Czwarta liga"),
        ("Piąta liga", "Piąta liga"),
        ("Klasa okręgowa", "Klasa okręgowa"),
        ("Klasa A", "Klasa A"),
        ("Klasa B", "Klasa B"),
        ("Klasa C", "Klasa C"),
    ]

    season = forms.ChoiceField(choices=SEASON_CHOICES)
    province = forms.ChoiceField(choices=PROVINCE_CHOICES)
    competition_class = forms.ChoiceField(choices=COMPETITION_CLASS_CHOICES)
    group = forms.CharField(max_length=200)


GROUP_CHOICES = {
    "dolnośląskie": {
        "Klasa B": [
            "Wałbrzych: Klasa B Grupa 5", "Wałbrzych: Klasa B Grupa 4", "Wałbrzych: Klasa B Grupa 3", "Wałbrzych: Klasa B Grupa 2", "Wałbrzych: Klasa B Grupa 1"
        ],
        "Klasa A": ["Wałbrzych: Klasa A Grupa 1", "Wałbrzych: Klasa A Grupa 2", "Wałbrzych: Klasa A Grupa 3"],
        "Klasa okręgowa": ["Wałbrzych: Klasa okręgowa"],
        "Czwarta liga": ['IV Liga "KOLEJE DOLNOŚLĄSKIE"']
    },
    "wielkopolskie": {
        "Klasa B": ['Klasa B "Proton" Grupa 1', 'Klasa B "Proton" Grupa 2', 'Klasa B "Proton" Grupa 3', 'Klasa B "Proton" Grupa 4', 'Klasa B "Proton" Grupa 5', 'Klasa B "Proton" Grupa 6', 'Klasa B "Proton" Grupa 7', 'Klasa B "Proton" Grupa 8', 'Klasa B "Proton" Grupa 9', 'Klasa B "Proton" Grupa 10', 'Klasa B "Proton" Grupa 11', 'Klasa B "Proton" Grupa 12', 'Klasa B "Proton" Grupa 13'],
        "Klasa A": ['Klasa A "Proton" Grupa 1', 'Klasa A "Proton" Grupa 2', 'Klasa A "Proton" Grupa 3', 'Klasa A "Proton" Grupa 4', 'Klasa A "Proton" Grupa 5', 'Klasa A "Proton" Grupa 6', 'Klasa A "Proton" Grupa 7'],
        "Klasa okręgowa": ['Klasa okręgowa "Red Box" Grupa 1', 'Klasa okręgowa "Red Box" Grupa 2', 'Klasa okręgowa "Red Box" Grupa 3', 'Klasa okręgowa "Red Box" Grupa 4', 'Klasa okręgowa "Red Box" Grupa 5', 'Klasa okręgowa "Red Box" Grupa 6'],
        "Piąta liga": ['Piąta liga "Red Box" Grupa 1', 'Piąta liga "Red Box" Grupa 2', 'Piąta liga "Red Box" Grupa 3'], 
        "Czwarta liga": ['IV Liga "Artbud Group"']
    },
    "kujawsko-pomorskie": {
        "Klasa B": ['Bydgoszcz: Klasa B "Inowrocław" Grupa 5', 'Bydgoszcz: Klasa B "Nakło-Bydgoszcz" Grupa 3', 'Bydgoszcz: Klasa B "Sępólno-Tuchola" Grupa 1'],
        "Klasa A": ['Bydgoszcz: Klasa A "Północ" Grupa 1', 'Bydgoszcz: Klasa A "Południe" Grupa 2', 'Toruń: Klasa A', 'Włocławek: Klasa A'],
        "Klasa okręgowa": ['Klasa okręgowa Grupa 1', 'Klasa okręgowa Grupa 2'],
        "Czwarta liga": ['IV Liga']
    },
    "lubelskie": {
        "Klasa B": ['Biała Podlaska: Klasa B Grupa 1', 'Biała Podlaska: Klasa B Grupa 2', 'Chełm: Klasa B', 'Lublin: Klasa B Grupa 1', 'Lublin: Klasa B Grupa 2', 'Lublin: Klasa B Grupa 3', 'Lublin: Klasa B Grupa 4'],
        "Klasa A": ['Biała Podlaska: Klasa A Grupa 1', 'Biała Podlaska: Klasa A Grupa 2', 'Chełm: Klasa A', 'Lublin: Klasa A Grupa 1', 'Lublin: Klasa A Grupa 2', 'Lublin: Klasa A Grupa 3', 'Zamość: Klasa A'],
        "Klasa okręgowa": ['Biała Podlaska: Klasa okręgowa "Macron"', 'Chełm: Klasa okręgowa "Macron"', 'Lublin: Klasa okręgowa "Macron"', 'Zamość: Klasa okręgowa "Macron"'],
        "Czwarta liga": ['IV Liga "Macron"']
    }
}
