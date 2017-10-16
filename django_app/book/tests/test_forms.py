from django.test import TestCase
from django.contrib.auth import get_user_model

from book.forms import BuyBookRegisterForm

MyUser = get_user_model()


class BuyBookRegisterFormTest(TestCase):
    # Valid Form Data
    def test_BuyBookRegisterForm_valid(self):
        form = BuyBookRegisterForm(data={
            "cover_img": "http://bookthumb.phinf.naver.net/cover/102/909/10290989.jpg?type=m1&udate=20170721",
            "title": "Do it! 점프 투 파이썬 (이미 50만 명이 '점프 투 파이썬'으로 시작했다!)",
            "author": "박응용",
            "publisher": "이지스퍼블리싱",
            "publication_date": "20160303",
            "normal_price": "18800",
            "isbn": "8997390910 9788997390915",
            "category": "프로그래밍언어",
            "used_price": "10000",
            "etc_requirements": "테스트",
        })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_BuyBookRegisterForm_invalid(self):
        form = BuyBookRegisterForm(data={
            "cover_img": "",
            "title": "Do it! 점프 투 파이썬 (이미 50만 명이 '점프 투 파이썬'으로 시작했다!)",
            "author": "박응용",
            "publisher": "이지스퍼블리싱",
            "publication_date": "20160303",
            "normal_price": "18800",
            "isbn": "8997390910 9788997390915",
            "category": "프로그래밍언어",
            "used_price": "10000",
            "etc_requirements": "테스트",
        })
        self.assertFalse(form.is_valid())


class SellBookRegisterFormTest(TestCase):
    def setUp(self):
        pass


class CommentFormTest(TestCase):
    def setUp(self):
        pass


class searchFormTest(TestCase):
    def setUp(self):
        pass