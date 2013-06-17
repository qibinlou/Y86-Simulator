from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect ,HttpResponse
from database.models import *
from django.db.models import Q

def home(request):
    source_code = SourceCode.objects.all()
    return render_to_response('index.html', locals())
