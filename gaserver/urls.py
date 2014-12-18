from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gaserver.views.api_root', name='api-root'),
    url(r'training/',
        include('training.urls', namespace='training', app_name='training')),
)
