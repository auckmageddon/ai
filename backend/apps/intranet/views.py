from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseForbidden
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings

from intranet.models import Server, BarTab
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
    if request.META["REMOTE_ADDR"] not in settings.HLSW_SERVERS:
        return HttpResponseForbidden()
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    server = AddServerForm(request.POST)
    if server.is_valid():
        try:
            server.instance = Server.objects.get(address=server.cleaned_data["address"])
        except Server.DoesNotExist:
            pass

        server.save()
        return HttpResponse()  # think of something more API-ish for this?
    else:
        return HttpResponseBadRequest()


def claim_bartab(request, code):
    bartab = get_object_or_404(BarTab, code=code)

    if bartab.claimed:
        return render_to_response('backend/bartab_claimed.html',
            RequestContext(request))
    else:
        bartab.claimed = True
        bartab.claimant = request.META["REMOTE_ADDR"]
        bartab.save()

        return render_to_response('backend/bartab_unclaimed.html',
            RequestContext(request,
                {'confirmation': bartab.confirmation,
                 'value': bartab.value}))
