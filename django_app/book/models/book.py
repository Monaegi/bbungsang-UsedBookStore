from django.conf import settings
from django.db import models

from member.models import Seller


class Book(models.Model):
    """ 책 기본(필수) 정보 """

    BOOK_TYPE_LANG = 'lang'
    BOOK_TYPE_OS = 'os'
    BOOK_TYPE_ALGORITHM = 'algorithm'
    BOOK_TYPE_NETWORK = 'network'
    BOOK_TYPE_DB = 'db'
    BOOK_TYPE_ETC = 'etc'
    BOOK_TYPE_CHOICES = (
        (BOOK_TYPE_LANG, '언어'),
        (BOOK_TYPE_OS, '운영체제'),
        (BOOK_TYPE_ALGORITHM, '자료구조/알고리즘'),
        (BOOK_TYPE_NETWORK, '네트워크'),
        (BOOK_TYPE_DB, '데이터베이스'),
        (BOOK_TYPE_ETC, 'etc(소프트웨어공학 등)'),
    )

    cover_img = models.CharField(max_length=200, )
    title = models.CharField(max_length=100, )
    author = models.CharField(max_length=50, )
    publisher = models.CharField(max_length=50, )
    publication_date = models.CharField(max_length=15, )
    isbn = models.CharField(max_length=50, )
    normal_price = models.CharField(max_length=25, blank=True)
    used_price = models.CharField(max_length=25, blank=True)
    category = models.CharField(
        max_length=50,
        choices=BOOK_TYPE_CHOICES,
    )

    buyer = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

    seller = models.ManyToManyField(
        Seller,
    )