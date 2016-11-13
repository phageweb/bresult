# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView
from bresult.models import Pair
from bresult.forms import PairForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User

class AboutView(TemplateView):
    template_name = "about.html"

class StartView(TemplateView):
    template_name = "base.html"

class PairList(ListView):
    model = Pair
    template_name = "pair_list.html"


def pair_new(request):
        if request.method == "POST":
            form = PairForm(request.POST)
            if form.is_valid():
                pair = form.save(commit=False)
                #pair.user_id = request.user
                pair.save()

                #return redirect('bresult.views.result_list', pk=result.pk)
        else:
            form = PairForm()
        return render(request, 'pair_new.html', {'form': form})

