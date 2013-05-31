from ilo.models import IloHost
from django.contrib import admin

admin.site.register(IloHost)


def create_test_data():
    """ Generate some test data """

    for line in open('/tmp/t').readlines():
        line = line.split('\t')
        if len(line) < 12:
            continue
        host_name = line[6]
        username = line[9]
        password = line[10]
        address = line[8]

        if not host_name:  # host name empty
            continue
        ilo = IloHost()
        ilo.host_name = host_name
        ilo.username = username
        ilo.password = password
        ilo.address = address
        print "Saving", host_name
        ilo.save()

