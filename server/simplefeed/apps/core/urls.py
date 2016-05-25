from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from core.views import *

from core.api import router

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls, namespace='api')),
    # url("^register/$", register, name="register"),
)
