from datetime import datetime, time
from django import forms

from playgames.models import PlayGame


class PlaygamesForm(forms.ModelForm):
    class Meta:
        model = PlayGame
        fields = [
            "team_local",
            "team_visitor",
            "score_local",
            "score_visitor",
            "week",
        ]
        
    # Remplacement du champ `played_at` par deux champs distincts
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date du match",
    )
    time = forms.ChoiceField(
        choices=[("14:00", "14:00"), ("18:00", "18:00")],  # Valeurs comme chaînes
        label="Heure du match",
    )

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time_selected = cleaned_data.get("time")

        if date and time_selected:
            # Dictionnaire pour mapper les chaînes à des objets `time`
            time_mapping = {
                "14:00": time(14, 0),
                "18:00": time(18, 0),
            }
            time_obj = time_mapping.get(time_selected)

            if time_obj is None:
                raise forms.ValidationError("L'heure sélectionnée est invalide.")

            # Combiner la date et l'heure en un datetime pour le champ `played_at`
            cleaned_data["played_at"] = datetime.combine(date, time_obj)

        return cleaned_data
