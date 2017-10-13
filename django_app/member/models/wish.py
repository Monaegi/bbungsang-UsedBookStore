from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from book.models import SellBookRegister


class BookWishList(TimeStampedModel):
    """ 위시리스트 """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        SellBookRegister,
        on_delete=models.CASCADE,
    )


class News(TimeStampedModel):
    """ 소식 받기 """

    my_follow = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    follow_other = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
    )
