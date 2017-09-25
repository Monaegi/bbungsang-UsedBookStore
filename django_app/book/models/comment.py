from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from book.models import SellBookRegister


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    sell_book = models.ForeignKey(
        SellBookRegister,
        on_delete=models.CASCADE,
    )

    content = models.TextField()
    star_score = models.IntegerField()