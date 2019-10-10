from django import template
import re

register = template.Library()


@register.filter
def s_list(arg1, arg2):
    arg = arg1.split(arg2)
    return arg


@register.filter
def s_replace(arg1):
    arg = re.sub(r'[\s.]+', '-', arg1)
    return arg

