LOCAL_SETTINGS = True
from settings import *

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('FACEBOOK_SECRET', '')
