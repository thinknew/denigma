from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"

urlpatterns = patterns("")

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )

urlpatterns += patterns("",
    url(r'^polls/', include('polls.urls')),
    url(r"^$", 'shorty.views.home', name='home'),
    url(r"^e/([^/]+)/", 'shorty.views.manage', name='source'),
    url(r"^a/", include(admin.site.urls)),
    url(r"^(\w+)/", 'shorty.views.visit', name='visit'),

)

