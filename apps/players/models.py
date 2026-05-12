from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('CB', 'Center Back'),
        ('LB', 'Left Back'),
        ('RB', 'Right Back'),
        ('LWB', 'Left Wing Back)'),
        ('RWB', 'Right Wing Back)'),

        ('CDM', 'Center Defensive Midfielder'),
        ('CM', 'Center Midfielder'),
        ('CAM', 'Center Attacking Midfielder'),
        ('LM', 'Left Midfielder'),
        ('RM', 'Right Midfielder'),

        ('LW', 'Left Winger'),
        ('RW', 'Right Winger'),
        ('CF', 'Center Forward'),
        ('ST', 'Striker'),

    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], unique=True)

    position = models.CharField(max_length=3, choices=POSITION_CHOICES)

    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    clean_sheets = models.PositiveIntegerField(default=0)

    red_cards = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"[{self.position}] {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = date.today()
        return (today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))






