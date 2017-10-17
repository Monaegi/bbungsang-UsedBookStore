import json
import urllib.request

import mock
import unittest

from django.conf import settings


class ExternalAPI:
    def import_naver_book_api(self, ):
        q = "파이썬"
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
            results_list = json.loads(response_body.decode('utf-8'))['items']
            return results_list


def list_search_result_sorted():
    pass


class TestNaverBookAPI(unittest.TestCase):
    @mock.patch.object(ExternalAPI, "import_naver_book_api")
    def test_search_result_sort(self, import_naver_book_api):
        print(import_naver_book_api)
        import_naver_book_api.return_value = ['Python', 'Java', 'C', 'Ruby', 'Golang']
        # results = list_search_result_sorted()
        # results = import_naver_book_api
        print(import_naver_book_api.return_value)

        # self.assertEqual(
        #     results,
        #     ['Python', 'Java', 'C', 'Ruby', 'Golang']
        # )

