"""Users urls."""
from django.conf.urls.defaults import *


urlpatterns = patterns('experts.views',
    (r'^whoiswho', 'whoiswho'),
    (r'^list', 'list'),
    (r'^', 'list')
)