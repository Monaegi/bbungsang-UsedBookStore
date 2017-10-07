from django.conf import settings
from django.db import models


class Seller(models.Model):
    """
    Seller 모델, MyUser 모델과 OTO 관계
    등록시 nickname, phone 필드는 필수 필드가 된다.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='my_seller',

    )


class EmailToken(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='email_token',
    )

    token = models.CharField(
        max_length=24,
    )