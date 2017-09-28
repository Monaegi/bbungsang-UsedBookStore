from django import template

register = template.Library()


@register.filter
def star(value):
    return "⭐" * value


@register.filter
def hide(value):
    return value.replace(value[4:], "*****")
