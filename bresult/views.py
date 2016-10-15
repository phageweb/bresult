# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView
from bresult.models import Result
from bresult.forms import ResultForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User

class AboutView(TemplateView):
    template_name = "about.html"

class ResultList(ListView):
    model = Result
    template_name = "result_list.html"

class StartView(TemplateView):
    template_name = "base.html"



def result_new(request):
        if request.method == "POST":
            form = ResultForm(request.POST)
            if form.is_valid():
                result = form.save(commit=False)
                result.user_id = request.user
                result.save()

                #return redirect('bresult.views.result_list', pk=result.pk)
        else:
            form = ResultForm()
        return render(request, 'result_new.html', {'form': form})

