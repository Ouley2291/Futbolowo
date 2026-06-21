from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ("kibic", "Kibic"),
        ("trener", "Trener"),
        ("zawodnik", "Zawodnik"),
        ("wlasciciel", "Właściciel klubu"),
        ("admin", "Administrator"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="kibic")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
