import requests
from django.conf import settings
from django.contrib import messages

from utils.apis import DebugTokenException


def get_facebook_access_token(request, code):
    exchange_access_token_url = 'https://graph.facebook.com/v2.9/oauth/access_token'

    redirect_uri = '{}{}'.format(
        settings.SITE_URL,
        request.path,
    )

    # 액세스토큰 요청시 필요한 파라미터
    exchange_access_token_url_params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': redirect_uri,
        'client_secret': settings.FACEBOOK_SECRET_CODE,
        'code': code,
    }

    response = requests.get(
        exchange_access_token_url,
        params=exchange_access_token_url_params,
    )

    result = response.json()

    # 응답받은 결과값에 'access_token'이라는 key가 존재하면,
    if 'access_token' in result:
        # access_token key의 value를 반환
        return result['access_token']
    elif 'error' in result:
        raise Exception(result)
    else:
        raise Exception('Unknown Error')


def facebook_debug_token(input_token):
    access_token = '{}|{}'.format(
        settings.FACEBOOK_APP_ID,
        settings.FACEBOOK_SECRET_CODE,
    )

    debug_token_url = 'https://graph.facebook.com/debug_token'

    debug_token_url_params = {
        'input_token': input_token,
        'access_token': access_token,
    }

    response = requests.get(debug_token_url, debug_token_url_params)
    result = response.json()

    if 'error' in result['data']:
        raise DebugTokenException(result)

    return result


def facebook_get_user_info(user_id, access_token):
    url_user_info = 'https://graph.facebook.com/v2.9/{user_id}'.format(user_id=user_id)
    url_user_info_params = {
        'access_token': access_token,
        'fields': ','.join([
            'id',
            'picture',
            'email',
        ])
    }
    response = requests.get(url_user_info, params=url_user_info_params)
    result = response.json()

    return result


def get_kakao_access_token(code):
    exchange_access_token_url = 'https://kauth.kakao.com/oauth/token'
    redirect_uri = settings.KAKAO_REDIRECT_URI
    exchange_access_token_url_params = {
        'grant_type': 'authorization_code',
        'client_id': settings.KAKAO_APP_ID,
        'redirect_uri': redirect_uri,
        'code': code,
        'client_secret': settings.KAKAO_CLIENT_SECRET,
    }
    response = requests.get(
        exchange_access_token_url,
        params=exchange_access_token_url_params,
    )
    result = response.json()

    # 응답받은 결과값에 'access_token'이라는 key가 존재하면,
    if 'access_token' in result:
        # access_token key의 value를 반환
        return result['access_token']
    elif 'error' in result:
        raise Exception(result)
    else:
        raise Exception('Unknown Error')


def kakako_app_connection(access_token):
    url = 'https://kapi.kakao.com/v1/user/signup'
    access_token = "Bearer " + access_token
    response = requests.get(
        url,
        headers={
            "Authorization": access_token,
            "Content-Type": "Content-Type: application/x-www-form-urlencoded;charset=utf-8",
        },
    )
    result = response.json()
    return result


def get_kakao_user_info(access_token):
    url = 'https://kapi.kakao.com/v1/user/me'
    response = requests.get(
        url,
        headers={
            "Authorization": "Bearer " + access_token,
        }
    )
    result = response.json()
    return result


# 공통 사용
def return_result(result):
    # 응답받은 결과값에 'access_token'이라는 key가 존재하면,
    if 'access_token' in result:
        # access_token key의 value를 반환
        return result['access_token']
    elif 'error' in result:
        raise Exception(result)
    else:
        raise Exception('Unknown Error')


def error_message_and_redirect_referer(request):
    error_message = 'Social Login Error'
    messages.error(request, error_message)
