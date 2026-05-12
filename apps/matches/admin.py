from django.contrib import admin

from .models import Match, MatchEvent

admin.site.register(Match)
admin.site.register(MatchEvent)
