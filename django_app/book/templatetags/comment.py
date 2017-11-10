import re
from django import template

register = template.Library()


@register.filter
def star(value):
    return "⭐" * value


@register.filter
def hide(value):
    return value.replace(value[4:], "*****")


@register.filter
def img_filter(value):
    p = re.compile('ht{2}p')
    rep = value.replace(value[:7], "")
    m = p.search(rep)
    if m:
        return True
    return False
