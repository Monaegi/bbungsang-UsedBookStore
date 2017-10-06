from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# debug 모드, allowed hosts
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['databases']

SITE_URL = 'http://localhost:8000'
KAKAO_REDIRECT_URI = SITE_URL + '/member/login/kakao'