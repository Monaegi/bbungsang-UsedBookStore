"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from member import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^books/', include('book.urls', namespace="book")),
    url(r'^$', views.login),

    url(r'^messages/', include('django_messages.urls')),
]
# /static/, /media/에 대한 요청을 STATIC_ROOT, MEDIA_ROOT 경로의 파일에서 찾는다.
# /xx/ URL 에 대해서 XX_ROOT 경로에서 파일을 찾아서 해당 파일 자체를 리턴
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
