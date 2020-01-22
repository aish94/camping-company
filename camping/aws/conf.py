import datetime
import os

AWS_USERNAME = "kanishk"
AWS_GROUP_NAME = "camping-company-group"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
#AWS_DEFAULT_ACL = None

AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = (
    "text/css",
    "text/javascript",
    "application/javascript",
    "application/x-javascript",
    "image/svg+xml"
)

DEFAULT_FILE_STORAGE = 'camping.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'camping.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'camping-company'
S3DIRECT_REGION = 'ap-south-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

one_year = datetime.timedelta(days=365)

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=%d' % (int(one_year.total_seconds()), ),
}

AWS_QUERYSTRING_AUTH = False
