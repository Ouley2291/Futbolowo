from django import forms
from .models import LeagueQuery

class LeagueQueryForm(forms.Form):    
    SEASON_CHOICES = [
        ("2023/2024", "2023/2024"),
        ("2024/2025", "2024/2025"),
        ("2025/2026", "2025/2026"),
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
    group = forms.CharField(max_length=100)

