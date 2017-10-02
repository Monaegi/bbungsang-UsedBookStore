from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    # api MyUser
    url(r'^api/signup/$', views.SignUpView.as_view(), name='api_signup'),
    url(r'^api/login/$', views.LogInView.as_view(), name='api_login'),

    # normal MyUser
    url(r'^login/$', views.login, name='login'),
    url(r'^login/facebook/$', views.facebook_login, name='facebook_login'),
    url(r'^login/kakao/$', views.kakao_login, name='kakao_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^seller/(?P<user_pk>\d+)/$', views.seller_register, name='seller_register'),
]