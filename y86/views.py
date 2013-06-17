from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect ,HttpResponse
from database.models import *
from django.db.models import Q
import json

def home(request):
    # source_code = SourceCode.objects.all()
    return render_to_response('index.html', locals())
    # return HttpResponse("hello")
    
def phase(request):
    if 'source_id' in request.GET and request.GET['source_id']:
        try:
            source = SourceCode.objects.get(id=request.GET['source_id'])
        except:
            pass
            #need to be done.
    else:
        HttpResponse("Source Code ID does not exist!")
    if 'step' in request.GET and request.GET['step']:
        try:    
            t_phase = Phase.objects.get(step=request.GET['step']).filter(source_code=source)
            register = json.load(t_phase.register)
            memory = json.load(t_phase.memory)
        except:
            pass
            #proc new phase and save
    else:
        HttpResponse("step does not exist!")
    
    
