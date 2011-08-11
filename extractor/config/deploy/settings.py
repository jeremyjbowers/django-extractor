from extractor.config.base.settings import *

try:
    from extractor.config.deploy.local_settings import *
except ImportError:
    pass

DEBUG                       = True
TEMPLATE_DEBUG              = DEBUG

MEDIA_ROOT                  = os.path.join(PROJECT_DIR, '%s/media' % (PROJECT_SLUG))
MEDIA_URL                   = ''

# GRAPPELLI SETTINGS
ADMIN_MEDIA_PREFIX          = 'http://preps.s3.amazonaws.com/static/grappelli/'

# DJANGO-STORAGES SETTINGS
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
DEFAULT_FILE_STORAGE        = 'storages.backends.s3.S3Storage'
AWS_STORAGE_BUCKET_NAME     = 'jeremybowerscom'

ADMINS = (
     ('Jeremy Bowers', 'jeremyjbowers@gmail.com'),
)
MANAGERS = ADMINS