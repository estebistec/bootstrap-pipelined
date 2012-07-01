

# from django.conf.urls import include
from django.conf.urls import patterns
# from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    (r'^/?$', TemplateView.as_view(template_name='index.html')),
    # Examples:
    # url(r'^$', 'bootstrap_pipelined.views.home', name='home'),
    # url(r'^bootstrap_pipelined/', include('bootstrap_pipelined.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
