from django.conf.urls import url

from . import views

app_name = 'book'
urlpatterns = [
    url(r'^main/$', views.main, name='main'),

    url(r'^search/$', views.naver_search_books, name='naver_search_books'),
    url(r'^buy/register/$', views.buy_book_register, name='buy_book_register'),
    url(r'^buy/list/$', views.buy_book_list, name='buy_book_list'),
    url(r'^buy/detail/(?P<pk>\d+)/$', views.buy_book_detail, name='buy_book_detail'),
]
