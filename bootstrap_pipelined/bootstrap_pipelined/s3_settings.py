

import os
from .settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

AWS_ACCESS_KEY_ID = os.environ['S3KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3SECRET']
AWS_STORAGE_BUCKET_NAME = os.environ['S3BUCKET']
AWS_S3_SECURE_URLS = True
# NOTE This could also be a CloudFront backed by the S3 bucket!
STATIC_URL = "http://{0}.s3.amazonaws.com/".format(os.environ['S3BUCKET'])
STATICFILES_STORAGE = 'bootstrap_pipelined.storage.S3PipelineStorage'
