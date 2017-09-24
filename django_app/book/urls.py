from django.conf.urls import url

from . import views

app_name = 'book'
urlpatterns = [
    url(r'^main/$', views.main, name='main'),

    url(r'^search/$', views.naver_search_books, name='naver_search_books'),
    url(r'^buy/register/$', views.buy_book_register, name='buy_book_register'),
    url(r'^buy/list/$', views.buy_book_list, name='buy_book_list'),
    url(r'^buy/detail/(?P<buy_pk>\d+)/$', views.buy_book_detail, name='buy_book_detail'),
    url(r'^sell/register/$', views.sell_book_register, name='sell_book_register'),
    url(r'^sell/list/$', views.sell_book_list, name='sell_book_list'),
    url(r'^sell/detail/(?P<sell_pk>\d+)/$', views.sell_book_detail, name='sell_book_detail'),
    url(r'^wishlist/(?P<book_pk>\d+)/$', views.book_wish_list, name='book_wish_list'),
]
