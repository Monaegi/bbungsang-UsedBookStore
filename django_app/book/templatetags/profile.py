import re
from django import template

register = template.Library()


@register.filter
def img_filter(value):
    """ 일반, 소셜 회원 이미지 필터 """

    p = re.compile('ht{2}p')
    rep = value.replace(value[:7], "")
    m = p.search(rep)
    if m:
        return True
    return False