# Create your views here.

from django.http import HttpResponse
from models import IloHost
from django.shortcuts import render_to_response, get_object_or_404
import hpilo

def index(request):
  hosts = IloHost.objects.all()
  return render_to_response("index.html", locals())


def detail(request, ilo_name):
  my_ilo = get_object_or_404(IloHost, host_name=ilo_name)
  
  try:
    ilo = hpilo.Ilo(hostname=my_ilo.address, login=my_ilo.username, password=my_ilo.password)
    host_data = ilo.get_host_data()
    basic_info = host_data[1]
    product_name = basic_info.get('Product Name')
    serial_number = basic_info.get('Serial Number')
  except hpilo.IloCommunicationError, error_description:
    error = error_description
  return render_to_response("detail.html", locals())




