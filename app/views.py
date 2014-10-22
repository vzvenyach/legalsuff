from django.shortcuts import render
from django.template import RequestContext
import json

from app.forms import SufficiencyForm
from app.models import Sufficiency

# Create your views here.

def add_memo(request):
    context = RequestContext(request)
    if request.method == "POST":
        f = SufficiencyForm(request.POST)
        sufficiency = f.save()
        print sufficiency
        # print json.dumps(json_data, indent=2)
    return render(request, 'add_memo.html', {'form': SufficiencyForm()}, context_instance=RequestContext(request))

def show_sufficiency(request, sufficiency_id):
    context = RequestContext(request)
    suffiency = Sufficiency.objects.get(pk=sufficiency_id)
    return render(request, 'show_sufficiency.html', {'s': suffiency}, context_instance=RequestContext(request))