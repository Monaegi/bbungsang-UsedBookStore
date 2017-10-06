from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# debug 모드, allowed hosts
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['database']