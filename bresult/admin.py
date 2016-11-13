from django.contrib import admin
from bresult.models import Person, Pair, Team, Tournament


class PersonAdmin(admin.ModelAdmin):
    list_display = ['user','database']

class PairAdmin(admin.ModelAdmin):
    list_display = ['id','person1','person2']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','pair1','pair2']


class ResultAdmin(admin.ModelAdmin):
    list_display = []

class TournamentAdmin(admin.ModelAdmin):
    list_display = []
#    actions = ('next_round',)
#    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(Team, TeamAdmin)
#admin.site.register(Result, ResultAdmin)
admin.site.register(Tournament, TournamentAdmin)

