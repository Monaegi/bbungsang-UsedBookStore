from django.conf import settings
from django.db import models

from member.models import Seller


class Book(models.Model):
    """ 책 기본(필수) 정보 """

    BOOK_TYPE_LANG = '프로그래밍언어'
    BOOK_TYPE_OS = '운영체제'
    BOOK_TYPE_ALGORITHM = '자료구조/알고리즘'
    BOOK_TYPE_NETWORK = '네트워크'
    BOOK_TYPE_DB = '데이터베이스'
    BOOK_TYPE_ETC = 'ETC'

    BOOK_TYPE_CHOICES = (
        (BOOK_TYPE_LANG, '언어'),
        (BOOK_TYPE_OS, '운영체제'),
        (BOOK_TYPE_ALGORITHM, '자료구조/알고리즘'),
        (BOOK_TYPE_NETWORK, '네트워크'),
        (BOOK_TYPE_DB, '데이터베이스'),
        (BOOK_TYPE_ETC, 'etc(소프트웨어공학 등)')
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
        choices=BOOK_TYPE_CHOICES
    )

    buyer = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )

    seller = models.ManyToManyField(
        Seller
    )

    def save(self, *args, **kwargs):
        self.remove_b_tag()
        super().save(*args, **kwargs)

    def remove_b_tag(self):
        ori_title = self.title
        ori_title = ori_title.replace("<b>", "")
        ori_title = ori_title.replace("</b>", "")
        self.title = ori_title
        ori_author = self.author
        ori_author = ori_author.replace("<b>", "")
        ori_author = ori_author.replace("</b>", "")
        self.author = ori_author
        ori_publisher = self.publisher
        ori_publisher = ori_publisher.replace("<b>", "")
        ori_publisher = ori_publisher.replace("</b>", "")
        self.publisher = ori_publisher