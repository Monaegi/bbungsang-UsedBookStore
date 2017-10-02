from django.conf import settings


# request 인자를 안 받으면 'facebook_tag() takes 0 positional arguments but 1 was given' 에러 발생
def facebook_tag(request):
    context = {
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'site_url': settings.SITE_URL,
    }
    return context


def kakao_tag(request):
    context = {
        'kakao_app_id': settings.KAKAO_APP_ID,
        'kakao_redirect_uri': settings.KAKAO_REDIRECT_URI,
    }
    return context