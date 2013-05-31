# Create your views here.

from django.http import HttpResponse
from models import IloHost
from django.shortcuts import render_to_response, get_object_or_404

import hpilo

def index(request):
  hosts = IloHost.objects.all()
  return render_to_response("index.html", locals())


def detail(request, host_name):
  my_ilo = get_object_or_404(IloHost, host_name=host_name)

  return render_to_response("detail.html", locals())


def update(request, host_name):
    """ Connect to ilo and update cached metadata """
    print host_name
    print "hello"
    my_ilo = get_object_or_404(IloHost, host_name=host_name)
    my_ilo.update()
    return render_to_response("update.html", locals())

