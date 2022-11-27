from django.contrib import admin
from .models import (
Playoff, 
Conference, 
Series, 
Division, 
Stadium,
Coach,
Team, 
Team_Coach,
Player,
Team_Player,
Game,
Game_Player,
Scout,
Team_Scout,
Referee,
Game_Referee
) 

admin.site.site_header = "Techchain x jr.NBA"

# Register your models here.
admin.site.register(Playoff)
admin.site.register(Conference)
admin.site.register(Series)
admin.site.register(Division)
admin.site.register(Stadium)
# admin.site.register(Coach)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'position', 'university')


admin.site.register(Team)
admin.site.register(Team_Coach)
admin.site.register(Player)
admin.site.register(Team_Player)
# admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'home', 'away', 'homeScore', 'awayScore')

admin.site.register(Game_Player)
admin.site.register(Scout)
admin.site.register(Team_Scout)
admin.site.register(Referee)
admin.site.register(Game_Referee)
