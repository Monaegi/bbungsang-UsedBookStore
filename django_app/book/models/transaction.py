from django.conf import settings
from django.db import models

from book.models import Book


class BuyBookRegister(models.Model):
    """ 사려는 책 등록 """

    book_info = models.ForeignKey(
        Book,
        related_name='buy_book_info'
    )

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='buyer_info'
    )

    used_price = models.CharField(max_length=50, )
    etc_requirements = models.TextField()


class SellBookRegister(models.Model):
    """ 팔려는 책 등록 """

    class Meta:
        ordering = ['-pk']

    book_info = models.ForeignKey(
        Book,
        related_name='sell_book_info'
    )

    seller = models.ForeignKey(
        'member.Seller',
        related_name='seller_info'
    )

    used_price = models.CharField(max_length=50, )

    description = models.TextField(blank=True)


class BookStatus(models.Model):
    """ 팔려는 책에 대한 상태 인증 사진 """

    sell_book_status = models.ForeignKey(
        SellBookRegister,
    )