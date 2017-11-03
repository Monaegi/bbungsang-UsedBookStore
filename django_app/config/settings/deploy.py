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
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# debug 모드, allowed hosts
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']


def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
       See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server"""
    from urllib.request import urlopen
    if not is_ec2_linux():
        return None
    try:
        response = urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
        ec2_ip = response.read().decode('utf-8')
        if response:
            response.close()
        return ec2_ip
    except Exception as e:
        print(e)
        return None


private_ip = get_linux_ec2_private_ip()
if private_ip:
    ALLOWED_HOSTS.append(private_ip)

# Database
DATABASES = config_secret_deploy['django']['databases']

SITE_URL = 'http://usedbookstore-dev.ap-northeast-2.elasticbeanstalk.com'
KAKAO_REDIRECT_URI = SITE_URL + '/member/login/kakao'