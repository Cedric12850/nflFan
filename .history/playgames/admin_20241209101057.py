from django.contrib import admin

from playgames.models import PlayGame
from team.forms import PlayGameForm

# Register your models here.
@admin.register(PlayGame)
class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('team_local', 'score_local', 'team_visitor', 'score_visitor')
    search_fields = ('team_local','team_visitor')
    list_filter = ('team_local','team_visitor')
    list_per_page = 10
    form = PlayGameForm

    admin.site.register(PlayGame, PlayGameAdmin )