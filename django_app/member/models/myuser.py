from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager, Permission
from rest_framework.authtoken.models import Token

from utils.fields.custom_image_fields import CustomImageField


class MyUserManager(DefaultUserManager):
    pass


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

    my_photo = CustomImageField(

    )

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

    # objects = MyUserManager()

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)