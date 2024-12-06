from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from team.models import Teams

class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = [
            'name',
            'town',
            'stadium',
            'division',
            'owner',
            'founded',
            'thumbnail',
            'colorOne',
            'colorTwo'
        ]
        widgets = {'founded': forms.SelectDateWidget(years=range(1920, 2024))}

class TeamSelectFormMixin(forms.ModelForm):
    def __init__(self, data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)