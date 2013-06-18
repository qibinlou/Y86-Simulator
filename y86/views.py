#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect ,HttpResponse
from database.models import *
from django.db.models import Q
from form import UploadFileForm
import json
import math
from pipeline.Y86API import *

def home(request):
    # source_code = SourceCode.objects.all()
    return render_to_response('index.html', locals())
    # return HttpResponse("hello")

def upload(request):

    for item in request.FILES.getlist('files'):
        content = item.readlines() 
        sc = SourceCode(name=item.name,code=json.dumps(content))
        sc.save()

        phase = Phase()
        phase.source_code = sc
        reg,mem = executeY86(None,None,content)
        phase.register,phase.memory = json.dumps(reg), json.dumps(mem)
        phase.save()

    return  HttpResponse(200)


   

    return HttpResponse("hello")
    
def phase(request):
    if 'source_id' in request.GET and request.GET['source_id']:
        try:
            source = SourceCode.objects.get(id=request.GET['source_id'])
            # print source.code
        except:
            pass
            #need to be done.
    else:
        HttpResponse("Source Code ID does not exist!")
    if 'cycle' in request.GET and request.GET['cycle']:
        register = {}
        memory = {}
        cycle = int(request.GET['cycle'])
        
        if Phase.objects.filter(source_code=source,cycle=cycle).exists():
            p = Phase.objects.filter(source_code=source).get(cycle=cycle)
            register, memory = json.loads(p.register), json.loads(p.memory)
            result = {"source_id": source.id, "reg":register,"memo":memory}
            print "ssss"
            return HttpResponse(json.dumps(result))
        else:
            print "sfj23242342"


        if cycle < source.max_cycle:
            temp_max_cycle = 1
        else:
            temp_max_cycle = source.max_cycle
            
        # print temp_max_cycle
        p = Phase.objects.filter(source_code=source).get(cycle=temp_max_cycle)
        # print p
        register, memory = json.loads(p.register), json.loads(p.memory)

        
        # for current_cycle in range(temp_max_cycle+1, cycle+1):
        #             register,memory = executeY86(register, memory)
        while register['total_cycle'] != cycle:
            register,memory = executeY86(register, memory)
        source.max_cycle = cycle
        source.save()

        phase = Phase()
        phase.source_code = source
        phase.register,phase.memory = json.dumps(register), json.dumps(memory)
        phase.cycle = register['total_cycle']
        phase.save()
        result = {"source_id": source.id, "reg":register,"memo":memory}
        return HttpResponse(json.dumps(result))






        # try:
        #     t_phase = Phase.objects.filter(source_code=source).get(cycle=int(request.GET['cycle']))
        #     register = json.loads(t_phase.register)
        #     memory = json.loads(t_phase.memory)
        # except Exception, e:
        #     try:
        #         if cycle < 
        #         print source.max_cycle
        #         p = Phase.objects.filter(source_code=source).get(cycle=source.max_cycle)
        #         print p
        #         register, memory = json.loads(p.register), json.loads(p.memory)
        #         print register['total_cycle']
        #         temp_max_cycle = 1 if cycle < source.max_cycle else source.max_cycle
        #         for current_cycle in range(temp_max_cycle, cycle+1):
        #             register,memory = executeY86(register, memory)
        #             # total_cycle = register['total_cycle']
                    # source.max_cycle = total_cycle
                    # source.save()
                    # phase = Phase()
                    # phase.source_code = source
                    # phase.register,phase.memory = json.dumps(register), json.dumps(memory)
                    # phase.cycle = total_cycle
                    # phase.save()
                

            # except Exception, e:
            #     print e
            # else:
            #     pass
            # finally:
            #     pass
            
        # finally:
            
    else:
        HttpResponse("step does not exist!")
    return HttpResponse(403)

    
