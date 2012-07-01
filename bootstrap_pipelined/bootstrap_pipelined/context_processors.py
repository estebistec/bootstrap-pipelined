

from django.conf import settings


def google_analytics_key(request):
    return {
        'GOOGLE_ANALYTICS_KEY': getattr(settings, 'GOOGLE_ANALYTICS_KEY', None)
    }
