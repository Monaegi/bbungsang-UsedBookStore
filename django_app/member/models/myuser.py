import string
import random

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager

from member.models.seller import EmailToken
from utils.fields import CustomImageField


class MyUserManager(DefaultUserManager):
    def get_or_create_facebook_user(self, user_info):
        username = user_info.get('email', '')
        my_photo = user_info.get('picture', '')
        nickname = '{}_{}'.format(
            self.model.USER_TYPE_FACEBOOK,
            user_info['id']
        )

        # username이 email 형태가 아니면 email 형태의 username을 작성하는 폼 호출
        if username == '':
            pass

        if username and self.model.objects.filter(username=username):
            user = self.model.objects.get(username=username)
        else:
            user = self.model.objects.create(
                username=username,
                user_type=self.model.USER_TYPE_FACEBOOK,
                my_photo=my_photo['data']['url'],
                nickname=nickname,
            )

        return user

    def get_or_create_kakao_user(self, user_info):
        username = user_info.get('kaccount_email', '')
        my_photo = user_info.get('properties', '')
        nickname = '{}_{}'.format(
            self.model.USER_TYPE_KAKAO,
            user_info['id'],
        )

        if username == '':
            pass

        if username and self.model.objects.filter(username=username):
            user = self.model.objects.get(username=username)

        else:
            user = self.model.objects.create(
                username=username,
                user_type=self.model.USER_TYPE_KAKAO,
                my_photo=my_photo['profile_image'],
                nickname=nickname,
            )

        return user


class MyUser(AbstractUser):
    """ 유저 모델, 모든 인증된 사용자는 책을 '사는 사람' 권한을 갖음 """

    USER_TYPE_DJANGO = 'd'
    USER_TYPE_FACEBOOK = 'f'
    USER_TYPE_KAKAO = 'k'
    USER_TYPE_CHOICES = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
        (USER_TYPE_KAKAO, 'Kakao'),
    )

    username = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'username'

    my_photo = CustomImageField()

    nickname = models.CharField(
        max_length=54,
        blank=False,
        unique=True,
    )

    phone = models.CharField(
        max_length=13,
        blank=True,
    )

    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_DJANGO,
    )

    wish_list = models.ManyToManyField(
        'book.SellBookRegister',
        through='member.BookWishList',
    )

    follow = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='member.News'
    )

    objects = MyUserManager()

    def email_token_generator(self, user_pk, size=35, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        token = ''.join(random.choice(chars) for _ in range(size))
        EmailToken.objects.get_or_create(user_id=user_pk, token=token)
        return token

    # def get_user_token(self, user_pk):
    #     return Token.objects.get_or_create(user_id=user_pk)
