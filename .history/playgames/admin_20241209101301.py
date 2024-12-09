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

class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'team_local', 'team_visitor', 'played_at', 'score_team_local', 'score_team_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('played_at',)
    date_hierarchy = 'played_at'
    autocomplete_fields = ('week', 'team_local', 'team_visitor')

admin.site.register(PlayGame, PlayGameAdmin)