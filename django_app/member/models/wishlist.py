from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from book.models import SellBookRegister


class BookWishList(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        SellBookRegister,
        on_delete=models.CASCADE,
    )