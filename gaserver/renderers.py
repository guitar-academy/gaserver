from rest_framework.renderers import BrowsableAPIRenderer
from . import VERSION


class GABrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['version'] = VERSION
        return context
