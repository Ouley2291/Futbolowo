from django.db import models


class LeagueQuery(models.Model):
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

    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    league_type = models.CharField(max_length=50, default="Niższe ligi", editable=False)
    province = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    competition_class = models.CharField(max_length=100, choices=COMPETITION_CLASS_CHOICES)
    group = models.CharField(max_length=100)
