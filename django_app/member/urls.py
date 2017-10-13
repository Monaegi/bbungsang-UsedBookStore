from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    # api MyUser
    # url(r'^api/signup/$', views.SignUpView.as_view(), name='api_signup'),
    # url(r'^api/login/$', views.LogInView.as_view(), name='api_login'),

    # normal MyUser
    url(r'^login/$', views.login, name='login'),
    url(r'^login/facebook/$', views.facebook_login, name='facebook_login'),
    url(r'^login/kakao/$', views.kakao_login, name='kakao_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<slug>\w+)/info/$', views.user_info, name='user_info'),
    url(r'^news/(?P<user_pk>\d+)/$', views.news, name='news'),
    url(r'^news/cancel/(?P<user_pk>\d+)/$', views.cancel_news, name='cancel_news'),
    url(r'^seller/(?P<user_pk>\d+)/$', views.seller_register, name='seller_register'),
    url(r'^email/authenticate/(?P<user_pk>\d+)/$', views.send_email, name='send_email'),
]