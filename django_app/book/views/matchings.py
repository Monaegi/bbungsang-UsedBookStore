import json
import urllib.request

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from book.forms.book_register import BuyBookRegisterForm
from book.forms.searchs import NaverBooksSearchForm
from book.models import BuyBookRegister, Book


def naver_search_books(request):
    q = request.GET.get('q')

    client_id = settings.NAVER_CLIENT_ID
    client_secret = settings.NAVER_CLIENT_SECRET
    enc_q = urllib.parse.quote(q)
    url = "https://openapi.naver.com/v1/search/book?query=" + enc_q + "&display=52&sort=count"
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    res = urllib.request.urlopen(req)
    rescode = res.getcode()

    if rescode == 200:
        response_body = res.read()
        results_list = json.loads(response_body.decode('utf-8'))['items']

        paginator = Paginator(results_list, 4)

        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        context = {
            'q': q,
            'results': results,
        }

        return render(request, 'book/naver_book_search.html', context)


def buy_book_register(request, ):
    if request.method == 'POST':
        form = BuyBookRegisterForm(data=request.POST)

        if form.is_valid():
            form.save(buyer=request.user)

            return HttpResponse('성공!')

    register_form = BuyBookRegisterForm()
    search_form = NaverBooksSearchForm()
    context = {
        'register_form': register_form,
        'search_form': search_form,
    }
    return render(request, 'book/buy_book_register.html', context)
