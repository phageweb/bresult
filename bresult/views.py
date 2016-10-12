# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView
from bresult.models import Person

class AboutView(TemplateView):
    template_name = "about.html"

class PersonList(ListView):
    model = Person
    template_name = "person_list.html"




