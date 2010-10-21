from django.http import HttpResponse
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

def checkserver(request):
    #c = Context({})
    return HttpResponse('YES')

def joinserver(request):
    try:
        if request.GET['user'] == 'Player':
            return HttpResponse("Set your hosts file so www.minecraft.net -> ip for speedmc.net")
    except MultiValueDictKeyError:
        pass
    return HttpResponse('ok')

@csrf_exempt
def getversion(request):
    import sys
    if request.method == 'POST':
        userName = request.POST['user']
        #p = request.POST['password']
        #version = request.POST['version']
        version = '1285241960000'
        downloadTicket = ''
        sessionID = ''
        return HttpResponse(':'.join((version, downloadTicket, userName, sessionID)))

    return HttpResponse('ok')
