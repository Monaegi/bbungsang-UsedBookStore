from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from member.models import Seller
from member.models.seller import EmailToken

MyUser = get_user_model()


def send_email(request, user_pk):
    if request.method == 'POST':
        user = MyUser.objects.get(pk=user_pk)
        email_token = user.email_token_generator(user.pk)

        mail_subject = '판매자 인증 이메일입니다.'
        mail_content = '판매자 등록페이지에 {} 와 일치하는 인증 번호를 입력하시면 인증이 완료됩니다.' \
                       '해당 페이지로 이동하기 : http://localhost:8000/member/seller/{}/'.format(
            email_token,
            user.pk,
        )
        send_mail(
            mail_subject,
            mail_content,
            'bbungsang@gmail.com',
            [user.username],
        )
        return redirect('member:seller_register', user_pk=user.pk)


def seller_register(request, user_pk):
    """ 판매자 등록 """

    if request.method == 'POST':
        email_token = request.POST.get('email_token', '')
        user = MyUser.objects.get(pk=user_pk)

        if user.email_token.token != email_token or email_token == '':
            raise ValueError('입력하신 값이 일치하지 않습니다.')

        Seller.objects.get_or_create(user=user)
        return redirect('book:main')
    return render(request, 'member/seller_register.html')