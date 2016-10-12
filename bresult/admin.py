from django.contrib import admin
from bresult.models import Person, Result


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']
    pass

class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ['id','person','result', 'number', ]




admin.site.register(Person, PersonAdmin)
admin.site.register(Result, ResultAdmin)

