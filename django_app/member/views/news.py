from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from member.models.wish import News

MyUser = get_user_model()


def news(request, user_pk):
    user = MyUser.objects.get(pk=user_pk)
    News.objects.get_or_create(
        my_follow=request.user,
        follow_other=user,
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cancel_news(request, user_pk):
    user = MyUser.objects.get(pk=user_pk)
    news = News.objects.get(
        my_follow=request.user,
        follow_other=user,
    )
    news.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
