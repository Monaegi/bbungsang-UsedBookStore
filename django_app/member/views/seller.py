from django.contrib.auth import get_user_model
from django.shortcuts import render

from member.models import Seller

MyUser = get_user_model()


def seller_register(request, user_pk):
    """ 판매자 등록 """

    if request.method == 'POST':
        user = MyUser.objects.get(pk=user_pk)
        Seller.objects.get_or_create(user=user)
        return render(request, 'common/main.html', )
    return render(request, 'member/seller_register.html')