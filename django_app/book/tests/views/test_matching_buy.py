from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from book.models import Book, BuyBookRegister

MyUser = get_user_model()


class Setup_Class(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="test@test.com",
            password="test1234",
            nickname="test",
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
        BuyBookRegister.objects.create(
            buyer=self.user,
            book_info=self.book,
            used_price="10000",
            etc_requirements="테스트",
        )
        self.buy_book_register_url = reverse("book:buy_book_register")
        self.list_url = reverse("book:buy_book_list")
        self.read_update_delete_url = reverse("book:buy_book_detail", kwargs={"buy_pk": "1"})


class BuyBookViewTest(Setup_Class):
    def test_buy_book_register(self):
        BuyBookRegister.objects.create(
            buyer=self.user,
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
            etc_requirements="테스트",
        )
        self.assertEqual(BuyBookRegister.objects.count(), 2)

    def test_buy_book_list(self):
        response = self.client.get(self.list_url, follow=True)
        self.assertEqual(response.status_code, 200)
        for test_equal in response.context['all_books']:
            self.assertEqual(test_equal.buyer.username, "test@test.com")
            self.assertEqual(test_equal.buyer.nickname, "test")
            self.assertEqual(test_equal.book_info.cover_img, "http://bookthumb.phinf.naver.net/cover/102/909/10290989.jpg?type=m1&udate=20170721")
            self.assertEqual(test_equal.book_info.title, "Do it! 점프 투 파이썬 (이미 50만 명이 '점프 투 파이썬'으로 시작했다!)")
            self.assertEqual(test_equal.book_info.author, "박응용")
            self.assertEqual(test_equal.book_info.publisher, "이지스퍼블리싱")
            self.assertEqual(test_equal.book_info.normal_price, "18800")
            self.assertEqual(test_equal.book_info.publication_date, "20160303")
            self.assertEqual(test_equal.book_info.isbn, "8997390910 9788997390915")
            self.assertEqual(test_equal.book_info.category, "프로그래밍언어")
            self.assertEqual(test_equal.used_price, "10000")
            self.assertEqual(test_equal.etc_requirements, "테스트")

    def test_buy_book_detail(self):
        response = self.client.get(self.read_update_delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['book'].book_info.isbn, "8997390910 9788997390915")
        self.assertEqual(response.context['book'].buyer.username, "test@test.com")
        self.assertEqual(response.context['book'].buyer.nickname, "test")
        self.assertEqual(response.context['book'].book_info.cover_img,
                         "http://bookthumb.phinf.naver.net/cover/102/909/10290989.jpg?type=m1&udate=20170721")
        self.assertEqual(response.context['book'].book_info.title, "Do it! 점프 투 파이썬 (이미 50만 명이 '점프 투 파이썬'으로 시작했다!)")
        self.assertEqual(response.context['book'].book_info.author, "박응용")
        self.assertEqual(response.context['book'].book_info.publisher, "이지스퍼블리싱")
        self.assertEqual(response.context['book'].book_info.normal_price, "18800")
        self.assertEqual(response.context['book'].book_info.publication_date, "20160303")
        self.assertEqual(response.context['book'].book_info.isbn, "8997390910 9788997390915")
        self.assertEqual(response.context['book'].book_info.category, "프로그래밍언어")
        self.assertEqual(response.context['book'].used_price, "10000")
        self.assertEqual(response.context['book'].etc_requirements, "테스트")

    def test_buy_book_update(self):
        pass

    def test_buy_book_delete(self):
        pass
