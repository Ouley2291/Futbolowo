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

    matches = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"[{self.position}] {self.first_name} {self.last_name}"
    
    @property
    def age(self):
        today = date.today()
        return (today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))

def sort_bys_position(players):
    new_list = []
    gk = players.filter(position="GK")
    cb = players.filter(position="CB")
    lb = players.filter(position="LB")
    rb = players.filter(position="RB")
    lwb = players.filter(position="LWB")
    rwb = players.filter(position="RWB")
    cdm = players.filter(position="CDM")
    cm = players.filter(position="CM")
    cam = players.filter(position="CAM")
    lm = players.filter(position="LM")
    rm = players.filter(position="RM")
    lw = players.filter(position="LW")
    rw = players.filter(position="RW")
    cf = players.filter(position="CF")
    st = players.filter(position="ST")

    new_list.extend(gk)
    new_list.extend(cb)
    new_list.extend(lb)
    new_list.extend(rb)
    new_list.extend(lwb)
    new_list.extend(rwb)
    new_list.extend(cdm)
    new_list.extend(cm)
    new_list.extend(cam)
    new_list.extend(lm)
    new_list.extend(rm)
    new_list.extend(lw)
    new_list.extend(rw)
    new_list.extend(cf)
    new_list.extend(st)

    return new_list




