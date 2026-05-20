from django.forms import ModelForm
from .models import LeagueQuery

class LeagueQueryForm(ModelForm):
    class Meta:
        model = LeagueQuery
        fields = ['season', 'province', 'competition_class', 'group']
