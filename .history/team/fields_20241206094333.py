

# Création du champs personnalisé pour les équipes par division
from collections.abc import Callable
from typing import Any
from django import forms
from django.db.models.manager import Manager
from django.db.models.query import QuerySet


class TeamChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset: Manager[Any] | QuerySet[Any] | None, *, empty_label: str | None = ..., required: bool = ..., widget: Any | None = ..., label: Any | None = ..., initial: Any | None = ..., help_text: str = ..., to_field_name: Any | None = ..., limit_choices_to: dict[str, Any] | Callable[[], Any] | None = ..., **kwargs: Any) -> None:
        super().__init__(queryset, empty_label=empty_label, required=required, widget=widget, label=label, initial=initial, help_text=help_text, to_field_name=to_field_name, limit_choices_to=limit_choices_to, **kwargs)