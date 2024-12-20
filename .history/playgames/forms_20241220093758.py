from datetime import datetime, time
from django import forms

from playgames.models import PlayGame, Season, Week
from playgames.widgets import CustomWidgets, TeamSelectWidget
from team.models import Teams


class PlaygamesForm(forms.ModelForm):
    # Ajout d'un champ personnalisé pour sélectionner la saison
    season = forms.ModelChoiceField(
        queryset=Season.objects.all(),
        label="Season",
        required=True,
        widget=CustomWidgets.select_input  # Appliquer le widget personnalisé ici
    )
    team_local = forms.ModelChoiceField(
        queryset=Teams.objects.all(),
        label="Local Team",
        widget=TeamSelectWidget()
    )
    team_visitor = forms.ModelChoiceField(
        queryset=Teams.objects.all(),
        label="Visitor Team",
        widget=TeamSelectWidget()
    )

    class Meta:
        model = PlayGame
        fields = [
            "team_local",
            "team_visitor",
            "score_local",
            "score_visitor",
            "season",
            "week",
            "played_at"
        ]
        widgets = {
            "score_local": CustomWidgets.integer_input,
            "score_visitor": CustomWidgets.integer_input,
            "week": CustomWidgets.select_input,
            "played_at": CustomWidgets.date_input
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialiser le champ "week" avec un queryset vide
        self.fields["week"].queryset = Week.objects.none()

        if "season" in self.data:
            try:
                season_id = int(self.data.get("season"))
                self.fields["week"].queryset = Week.objects.filter(season_id=season_id).order_by("week_number")
            except (ValueError, TypeError):
                pass  # Si la saison est invalide
        elif self.instance.pk:
            # Pré-remplir les semaines si un objet existe déjà
            self.fields["week"].queryset = self.instance.week.season.weeks.all()