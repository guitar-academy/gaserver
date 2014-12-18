from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import api_root

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', api_root, name='api-root'),
    url(r'training/',
        include('training.urls', namespace='training', app_name='training')),
)
