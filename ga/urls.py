from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import api_root

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', api_root, name='api-root'),
    url(r'training/',
        include('training.urls', namespace='training', app_name='training')),

    # TokenAuthentication
    url(r'^token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    # SessionAuthentication
    url(r'^session-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

)
