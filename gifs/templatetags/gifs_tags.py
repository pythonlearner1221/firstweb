from ..models import GifPics
from django import template


register = template.Library()

@register.simple_tag
def archives():
    return GifPics.objects.dates('created_time','month',order='DESC')

