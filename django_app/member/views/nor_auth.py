from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, get_user_model

from member.forms import LoginForm
from utils.apis import get_facebook_access_token, facebook_debug_token, facebook_get_user_info, \
    get_kakao_access_token, error_message_and_redirect_referer, GetAccessTokenException, \
    DebugTokenException, get_kakao_user_info

MyUser = get_user_model()


def login(request):
    """ 일반 로그인 """

    form = LoginForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('book:main')
    else:
        if request.user.is_authenticated():
            return redirect('book:main')
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)


def logout(request):
    """ 로그아웃 """

    django_logout(request)
    return redirect('member:login')


def facebook_login(request):
    """ 페이스북 로그인 """

    code = request.GET.get('code')

    # code가 없으면 에러 메세지를 request에 추가하고 이전 페이지로 redirect
    if not code:
        return error_message_and_redirect_referer(request)

    try:
        access_token = get_facebook_access_token(request, code)
        debug_result = facebook_debug_token(access_token)
        user_info = facebook_get_user_info(user_id=debug_result['data']['user_id'], access_token=access_token)
        user = MyUser.objects.get_or_create_facebook_user(user_info)

        django_login(request, user)
        return redirect('book:main')
    except GetAccessTokenException as e:
        print(e.code)
        print(e.message)
        return error_message_and_redirect_referer(request)
    except DebugTokenException as e:
        print(e.code)
        print(e.message)
        return error_message_and_redirect_referer(request)


def kakao_login(request):
    """ 카카오 로그인 """

    code = request.GET.get('code')

    if not code:
        return error_message_and_redirect_referer(request)

    try:
        access_token = get_kakao_access_token(code)
        # app_connection = app_connection(access_token)
        user_info = get_kakao_user_info(access_token)
        print(user_info)
        user = MyUser.objects.get_or_create_kakao_user(user_info)

        django_login(request, user)
        return redirect('book:main')
    except GetAccessTokenException as e:
        print(e.code)
        print(e.message)
        return error_message_and_redirect_referer(request)
    except DebugTokenException as e:
        print(e.code)
        print(e.message)
        return error_message_and_redirect_referer(request)

