from django.contrib import admin
from bresult.models import Person, Result, Tournament


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']
    pass

class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ['user_id','result', 'number', ]
    pass

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['round', ]
    actions = ('next_round',)
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Tournament, TournamentAdmin)

