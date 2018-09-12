from django.shortcuts import render,render_to_response
from django.http import HttpRequest
from django import template
from unifieddbms.models import *

# Create your views here.
def index(request):
    result = host_info.objects.all().order_by('server_id')
    dic = {'result':result}
    return render_to_response('index.html',dic)