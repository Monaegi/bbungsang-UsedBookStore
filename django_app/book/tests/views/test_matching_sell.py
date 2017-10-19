from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from book.models import Book, SellBookRegister, BookStatus
from book.views import sell_book_detail
from member.models import Seller

MyUser = get_user_model()


class Setup_Class(TestCase):
    def setUp(self):
        self.seller = Seller.objects.create(
            user=MyUser.objects.create_user(
                username="test@test.com",
                password="test1234",
                nickname="test",
            )
        )
        self.book = Book.objects.create(
            cover_img="http://bookthumb.phinf.naver.net/cover/102/909/10290989.jpg?type=m1&udate=20170721",
            title="Do it! 점프 투 파이썬 (이미 50만 명이 '점프 투 파이썬'으로 시작했다!)",
            author="박응용",
            publisher="이지스퍼블리싱",
            normal_price="18800",
            publication_date="20160303",
            isbn="8997390910 9788997390915",
            category="프로그래밍언어",
        )
        self.sell_info = SellBookRegister.objects.create(
            seller=self.seller,
            book_info=self.book,
            used_price="10000",
            description="테스트"
        )
        sell_book_status = ["test.png", "test.png", "test.png", "test.png"]
        for i in range(len(sell_book_status)):
            BookStatus.objects.create(
                sell_book_status=self.sell_info,
                photo=sell_book_status[i],
            )
        self.sell_book_register_url = reverse('book:sell_book_register')
        self.read_update_delete_url = reverse("book:sell_book_detail", kwargs={"sell_pk": "1"})

        self.factory = RequestFactory()


class SellBookViewTest(Setup_Class):
    def test_sell_book_register(self):
        request = self.factory.get(self.sell_book_register_url)
        request.user = self.seller.user

        sell_info = SellBookRegister.objects.create(
            seller=request.user.my_seller,
            book_info=Book.objects.create(
                cover_img="http://bookthumb.phinf.naver.net/cover/118/232/11823284.jpg?type=m1&udate=20170328",
                title="Hello Coding 그림으로 개념을 이해하는 알고리즘",
                author="아디트야 바르가바",
                publisher="한빛미디어",
                normal_price="22000",
                publication_date="20170401",
                isbn="896848354X 9788968483547",
                category="자료구조/알고리즘",
            ),
            used_price="15000",
            description="테스트",
        )

        sell_book_status = ["test.png", "test.png", "test.png", "test.png"]

        for i in range(len(sell_book_status)):
            BookStatus.objects.create(
                sell_book_status=sell_info,
                photo=sell_book_status[i],
            )

        self.assertEqual(SellBookRegister.objects.count(), 2)

    def test_sell_book_detail(self):
        request = self.factory.get(self.read_update_delete_url)
        request.user = AnonymousUser()
        response = sell_book_detail(request, 1)
        self.assertEqual(response.status_code, 200)
        print(response.content.decode('utf-8'))
