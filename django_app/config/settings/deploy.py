from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['django']['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['django']['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['django']['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['django']['aws']['s3_region']
S3_USE_SIGV4 = True

# Storage settings
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# Static URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# debug 모드, allowed hosts
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['databases']

SITE_URL = 'http://usedbookstore-dev.ap-northeast-2.elasticbeanstalk.com'
KAKAO_REDIRECT_URI = SITE_URL + '/member/login/kakao'