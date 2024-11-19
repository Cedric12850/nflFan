from django.contrib import admin

from team.models import Coachs, Conferences, Divisions, PLayers, Teams


# Register your models here.
admin.site.register(Teams)
admin.site.register(PLayers)
admin.site.register(Coachs)
admin.site.register(Divisions)
admin.site.register(Conferences)
