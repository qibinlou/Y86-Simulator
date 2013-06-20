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
    files = []
    sources = SourceCode.objects.all()
    for item in sources:
        code = {}
        code['name'] = item.name
        code['id']= item.id
        files.append(code)
    print files
    
    return render_to_response('index.html', locals())
    # return HttpResponse("hello")

def upload(request):

    result = {}
    for item in request.FILES.getlist('files'):
        if SourceCode.objects.filter(name=item.name).exists():
            result[item.name] = SourceCode.objects.get(name=item.name).id
            continue
        content = item.readlines() 
        sc = SourceCode(name=item.name,code=json.dumps(content))
        sc.save()
        result[item.name] = sc.id

        phase = Phase()
        phase.source_code = sc
        #print content
        reg,mem = executeY86(None,None,content)
        # print reg['total_cycle']
        del content
        phase.register,phase.memory = json.dumps(reg), json.dumps(mem)
        phase.save()

    return  HttpResponse(json.dumps(result))


   

    return HttpResponse("hello")
    
def phase(request):
    if 'source_id' in request.GET and request.GET['source_id']:
        try:
            source = SourceCode.objects.get(id=request.GET['source_id'])
            # #print source.code
        except:
            pass
            #need to be done.
    else:
        HttpResponse("Source Code ID does not exist!")
    if 'cycle' in request.GET and request.GET['cycle']:
        register = {}
        memory = {}
        cycle = int(request.GET['cycle'])
        
        if Phase.objects.filter(source_code=source , cycle=cycle).exists():
            p = Phase.objects.filter(source_code=source).get(cycle=cycle)
            register, memory = json.loads(p.register), json.loads(p.memory)
            result = {"source_id": source.id, "reg":register,"memo":memory}
            #print "ssss"
            return HttpResponse(json.dumps(result))
        else:
            #print "sfj23242342"
            pass


        if cycle < source.max_cycle:
            temp_max_cycle = 1
        else:
            temp_max_cycle = source.max_cycle
            
        # #print temp_max_cycle
        p = Phase.objects.filter(source_code=source).get(cycle=temp_max_cycle)
        # #print p
        register, memory = json.loads(p.register), json.loads(p.memory)
        


        
        # for current_cycle in range(temp_max_cycle+1, cycle+1):
        #             register,memory = executeY86(register, memory)
        while (register['total_cycle'] < cycle) and (register['end'] != True):
            # print register,memory
            register,memory = executeY86(register, memory)
        source.max_cycle = register['total_cycle']
        source.save()

        phase = Phase()
        phase.source_code = source
        phase.register,phase.memory = json.dumps(register), json.dumps(memory)
        phase.cycle = register['total_cycle']
        if not Phase.objects.filter(source_code=phase.source_code).filter(cycle=phase.cycle).exists():
            phase.save()
        #print register
        result = {"source_id": source.id, "reg":register,"memo":memory}
        return HttpResponse(json.dumps(result))
    else:
        HttpResponse("step does not exist!")
    return HttpResponse(403)

    

def getcode(request):
    if 'source_id' in request.GET and request.GET['source_id']:
        try:
            source = SourceCode.objects.get(id=request.GET['source_id'])
            html = """
             <script src="/static/js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="/static/js/shCore.js"></script>
    <script type="text/javascript" src="/static/js/shBrushPhp.js"></script>
    <!-- <link type="text/css" rel="stylesheet" href="/static/css/shCoreDefault.css"> -->
    <link rel="stylesheet" type="text/css" href="/static/css/shCoreFadeToGrey.css">
    <link rel="stylesheet" type="text/css" href="/static/css/code.css">
    <script type="text/javascript">
        SyntaxHighlighter.defaults['first-line'] = 0;
        SyntaxHighlighter.all();
    </script>
        <pre class="brush: php;" contenteditable id="yocode">
        %s</pre>
            """ % ("".join(json.loads(source.code)))
            return HttpResponse(html)
        except:
            return HttpResponse(404)
    else:
        return HttpResponse(403)
