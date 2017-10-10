from django.conf.urls import url

from . import views

app_name = 'book'
urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^search/$', views.naver_search_books, name='naver_search_books'),

    # 책 사기
    url(r'^buy/register/$', views.buy_book_register, name='buy_book_register'),
    url(r'^buy/list/$', views.buy_book_list, name='buy_book_list'),
    url(r'^buy/detail/(?P<buy_pk>\d+)/$', views.buy_book_detail, name='buy_book_detail'),

    # 책 팔기
    url(r'^sell/register/$', views.sell_book_register, name='sell_book_register'),
    url(r'^sell/list/$', views.sell_book_list, name='sell_book_list'),
    url(r'^sell/detail/(?P<sell_pk>\d+)/$', views.sell_book_detail, name='sell_book_detail'),

    # 위시리스트
    url(r'^wish/list/$', views.book_wish_list, name='book_wish_list'),
    url(r'^wish/detail/(?P<book_pk>\d+)/$', views.book_wish_detail, name='book_wish_detail'),

    # 댓글
    url(r'^comment/create/(?P<sell_pk>\d+)$', views.create_comment, name='create_comment'),

    # 쪽지 커스텀
    url(r'^messages/reply/(?P<message_id>\d+)$', views.create_reply, name='create_reply'),
    url(r'^messages/inbox/$', views.inbox, name='inbox'),
    url(r'^messages/outbox/$', views.outbox, name='outbox'),
]
