# Split tag for imageboard

from django import template

register = template.Library()

@register.filter(name='split')
def split_filter(value):
    return value.split()