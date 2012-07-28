from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from models import Server
from forms import AddServerForm

@csrf_exempt
def add_server(request):
    """
    Adds a server to the database.  Server models use auto_now=True, so
    setting last_seen is not necessary (Django will automatically set it on
    save).
    
    Using the server ModelForm allows us to perform any input validation that
    we need to in there.  We may want to add some form of ACL 
    (settings.ALLOWED_TO_UPDATE_SERVERS = []?) for controlling this resource.
    """
    if request.method == "POST" and request.META["REMOTE_ADDR"] in settings.HLSW_SERVERS:
        server = AddServerForm(request.POST)
        if server.is_valid():
            try:
                old_server = Server.objects.get(address=server.cleaned_data["address"])
                server.instance = old_server
            except Server.DoesNotExist, e:
                pass
                
            server.save()
            return HttpResponse() # think of something more API-ish for this?
        else:
            return HttpResponseBadRequest()
    elif request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    else:
        return HttpResponseForbidden()