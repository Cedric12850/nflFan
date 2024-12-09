from django.contrib import admin

from playgames.models import PlayGame, Week

# Register your models here.
@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Personnalisez si nécessaire

class PlayGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'team_local', 'team_visitor', 'played_at', 'score_local', 'score_visitor')
    list_filter = ('week__season', 'week', 'played_at')
    search_fields = ('team_local__name', 'team_visitor__name')
    ordering = ('played_at',)
    date_hierarchy = 'played_at'
    autocomplete_fields = ('week', 'team_local', 'team_visitor')

admin.site.register(PlayGame, PlayGameAdmin)
admin.site.register(Week, w)