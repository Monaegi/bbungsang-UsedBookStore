from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager, Permission
from rest_framework.authtoken.models import Token

from utils.fields import CustomImageField


class MyUserManager(DefaultUserManager):
    def get_or_create_facebook_user(self, user_info):
        username = user_info.get('email', '')
        # my_photo =
        nickname = '{}_{}'.format(
            self.model.USER_TYPE_FACEBOOK,
            user_info['id']
        )

        # username이 email 형태가 아니면 email 형태의 username을 작성하는 폼 호출
        if username == '':
            pass

        user, user_created = self.get_or_create(
            username=username,
            user_type=self.model.USER_TYPE_FACEBOOK,
            # my_photo=
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
        max_length=36,
        blank=True,
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

    objects = MyUserManager()

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)