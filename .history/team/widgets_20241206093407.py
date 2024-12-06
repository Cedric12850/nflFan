from typing import Any, Sequence
from django.forms import Select
from django.forms.widgets import _OptAttrs


class TeamGroupedSelected(Select):
    def __init__(self, attrs: dict[str, Any] | None = ..., choices: Sequence[tuple[Any, Any]] = ...) -> None:
        super().__init__(attrs, choices)
