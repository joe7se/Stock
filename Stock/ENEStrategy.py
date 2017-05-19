from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import json
from .ENE import EneQuotaUtil
from .ENE import EneParameterRange

def ENE(request):
    return render_to_response('ENE.html')
#     return HttpResponse("Hello world ! ")

def ENE_training(request):
    code = request.GET.get('code')
    start = request.GET.get('start')
    end = request.GET.get('end')
    p = EneQuotaUtil()
    eneparam = EneParameterRange()
    eneparam.setCode(code)
    eneparam.setDaysMax(10)
    eneparam.setDaysMin(3)
    eneparam.setLowerMax(12)
    eneparam.setLowerMin(9)
    eneparam.setUpperMax(12)
    eneparam.setUpperMin(9)
    optimumParamList=p.get_Optimum_Param(eneparam)
    jsonData=[]
    for eneparam in optimumParamList:
        jsonData.append(json.dumps({
        	'upper': str(eneparam.get_upper()),
        	'lower': str(eneparam.get_lower()),
        	'days': str(eneparam.get_days()),
    	}))
    return HttpResponse(jsonData,content_type="application/json")
