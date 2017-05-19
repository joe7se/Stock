from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json
from .ENE.EneQuotaUtil import EneQuotaUtil
from .ENE.EneParameterRange import EneParameterRange

def ENE(request):
    return render_to_response('ENE.html')
#     return HttpResponse("Hello world ! ")

def ENE_training(request):
    code = request.GET.get('code')
    start = request.GET.get('start')
    end = request.GET.get('end')
    p = EneQuotaUtil()
    eneparam = EneParameterRange()
    eneparam.set_code(code)
    eneparam.setDays([3,4,5,6,7,8,9,10])
#     eneparam.set_days_min(3)
    eneparam.set_lower_max(12)
    eneparam.set_lower_min(9)
    eneparam.set_upper_max(12)
    eneparam.set_upper_min(9)
    
    
    eneparam.set_start_date(start[0:4],start[5:7],start[8:10])
    eneparam.set_end_date(end[0:4],end[5:7],end[8:10])
    optimumParamList=p.get_Optimum_Param(eneparam)
    result=[]
    for eneparam in optimumParamList:
        upper = eneparam.get_upper();
        lower = eneparam.get_lower();
        days = eneparam.get_days();
        result.append({'upper':upper,
                       'lower':lower,
                       'days':days,});
        
    jsonData = json.dumps(result);
    print jsonData
    return HttpResponse(jsonData,content_type="application/json")
