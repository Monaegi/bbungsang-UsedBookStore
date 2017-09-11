import json
import urllib.request

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from book.forms.book_register import BuyBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm


def naver_search_books(request):
    q = request.GET.get('q')
    print(q)
    # search_form = NaverBooksSearchForm(data=request.POST)
    #
    # if search_form.is_valid():

    client_id = settings.NAVER_CLIENT_ID
    client_secret = settings.NAVER_CLIENT_SECRET
    enc_q = urllib.parse.quote(q)
    url = "https://openapi.naver.com/v1/search/book?query=" + enc_q + "&display=5&sort=count"
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    res = urllib.request.urlopen(req)
    rescode = res.getcode()

    if rescode == 200:
        response_body = res.read()

        context = {
            'q': q,
            'results': json.loads(response_body.decode('utf-8'))['items'],
        }
        return render(request, 'book/naver_book_search.html', context)


def buy_book_register(request, ):
    if request.method == 'POST':
        pass
    register_form = BuyBookRegisterForm()
    search_form = NaverBooksSearchForm()
    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/buy_book_register.html', context)
