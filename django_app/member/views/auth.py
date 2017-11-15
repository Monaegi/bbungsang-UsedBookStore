from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, get_user_model

from book.models import SellBookRegister, BuyBookRegister
from member.forms import LoginForm
from member.forms.profile import ProfileForm
from member.forms.signup import SignupForm, BasicInfoForm
from member.models.wish import News
from utils.apis import get_facebook_access_token, facebook_debug_token, facebook_get_user_info, \
    get_kakao_access_token, error_message_and_redirect_referer, GetAccessTokenException, \
    DebugTokenException, get_kakao_user_info

MyUser = get_user_model()


def check_basic_info(request):
    """ 기본 정보 입력 """

    if request.method == "POST":
        form = BasicInfoForm(data=request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']
            request.session['nickname'] = form.cleaned_data['nickname']
            return redirect('member:signup')
    else:
        form = BasicInfoForm()
    context = {
        'form': form,
    }
    return render(request, 'member/input_basic_info.html', context)


def signup(request):
    """ 회원가입 """

    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    my_photo = request.POST.get('my_photo')
    slug = request.POST.get('slug')

    if request.method == "POST":

        if request.POST.get('user_type') == 'f':
            my_photo = request.POST.get('my_photo')
            social_photo = request.POST.get('social_photo')
            slug = request.POST.get('slug')

            if my_photo == '':
                my_photo = social_photo

            user = MyUser.objects.get(slug=slug)
            django_login(request, user)

            form = ProfileForm(
                data={
                    'username': request.POST.get('username'),
                    'my_photo': my_photo,
                    'nickname': request.POST.get('nickname'),
                    'phone': request.POST.get('phone', ''),
                },
                instance=request.user
            )

            if form.is_valid():
                form.save()
                return redirect('book:main')

        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = MyUser.objects.create_user(
                username=request.POST.get('username'),
                password=form.cleaned_data['password1'],
                my_photo=request.FILES.get('my_photo'),
                nickname=request.POST.get('nickname'),
                phone=request.POST.get('phone'),
            )
            user.save()
            return redirect('member:complete_signup')
    else:
        # return redirect('member:check_basic_info')
        form = SignupForm()
        username = request.session['username']
        nickname = request.session['nickname']
    context = {
        'form': form,
        'username': username,
        'nickname': nickname,
        'my_photo': my_photo,
        'slug': slug,
    }
    return render(request, 'member/signup.html', context)


def complete_signup(request):
    return render(request, 'member/complete_signup.html')


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

        if user.username == '':
            pass

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
        user_info = get_kakao_user_info(access_token)
        user = MyUser.objects.get_or_create_kakao_user(user_info)

        if user.username == '':
            context = {
                'nickname': user.nickname,
                'my_photo': str(user.my_photo),
                'slug': user.slug,
                'form': BasicInfoForm(),
            }
            return render(request, 'member/input_basic_info.html', context)

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


def user_info(request, slug):
    """ 판매자, 구매자 정보 조회 """

    user = MyUser.objects.get(nickname=slug)
    sell_books = SellBookRegister.objects.filter(seller=user.my_seller)
    buy_books = BuyBookRegister.objects.filter(buyer=user)
    news = News.objects.filter(
        my_follow=request.user,
        follow_other=user,
    )

    register_count = sell_books.count() + buy_books.count()
    follower_count = News.objects.filter(my_follow=user).count()
    following_count = News.objects.filter(follow_other=user).count()

    context = {
        'sell_books': sell_books,
        'buy_books': buy_books,
        'user_info': user,
        'news': news,
        'register_count': register_count,
        'follower_count': follower_count,
        'following_count': following_count,
    }
    return render(request, 'member/user_info.html', context)


def mypage(request, ):
    """ 회원 정보 조회, 수정 """
    pass


def withdrawal(request, ):
    """ 회원 탈퇴 """
    pass
