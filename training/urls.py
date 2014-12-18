from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import SongViewSet, SkillViewSet, WarmUpViewSet

router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'warm-ups', WarmUpViewSet)

urlpatterns = patterns('training.views',
    url(r'^$', 'api_root', name='api-root'),
) + router.urls
