from django.db import models

class League(models.Model):
    competition_class = models.CharField(max_length=50)
    group = models.CharField(max_length=200)
    province = models.CharField(max_length=50)
    season = models.CharField(max_length=10)

class LeagueStanding(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="positions")
    position = models.CharField(max_length=3)
    team = models.CharField(max_length=50)
    match_count = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    win_count = models.PositiveIntegerField(default=0)
    draw_count = models.PositiveIntegerField(default=0)
    loose_count = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    goals_balance = models.IntegerField(default=0)
