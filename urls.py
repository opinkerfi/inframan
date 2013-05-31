from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inframan.views.home', name='home'),
    # url(r'^inframan/', include('inframan.foo.urls')),
    url(r'^$', 'inframan.ilo.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<ilo_name>.+)/?$', 'inframan.ilo.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
