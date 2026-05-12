from django.db import models
from apps.players.models import Player
from django.core.validators import MinValueValidator, MaxValueValidator

class Match(models.Model):
    opponent = models.CharField(max_length=255)
    date = models.DateTimeField()

    home_match = models.BooleanField(default=True)

    our_score = models.PositiveIntegerField(default=0)
    opponent_score = models.PositiveIntegerField(default=0)

    competition = models.CharField(max_length=255, blank=True)
    stadium = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"vs {self.opponent}"


# Klasa reprezentujaca wydarzenia podczas meczu
class MatchEvent(models.Model):
    # Mozliwe Wydarzenia
    EVENT_CHOICES = [
        ("G", "Goal"),
        ("RC", "Red Card"),
        ("YC", "Yellow Card")
    ]

    type = models.CharField(max_length=2,choices=EVENT_CHOICES)

    # ForeingKey sluzy do laczania dwoch tabeli w relacje
    # tutaj przypisujemy odpowiedniego gracza do naszego wydarzenia
    # on_delete=models.CASCADE - mowi ze jesli gracz zostanie usuniety z tabeli players to wszystkie wydarzenia do ktorych
    # byl przypisany rowniez zostana usuniete z tabeli MatchEvent
    # related name to po prostu sposob na odwolanie sie do wszystkich MatchEvent do ktorych przypisany byl gracz np wydarzenia = player.events
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="events") 
    match = models.ForeignKey(Match,on_delete=models.CASCADE, related_name="events")

    minute = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(130)])

    # Gracz ktory asystowal (null=True i blank=True), poniewaz nie trzeba go przypisawac do eventu
    # jest on tylko opcjonalny
    assist_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="assisted_goals", null=True, blank=True) 

    def __str__(self):
        return f"{self.player} - {self.event_type}"

