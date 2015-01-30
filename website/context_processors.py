import os
import socket
import datetime

from models import Category, Subcategory, Product
from django.conf import settings

def shared(request):
    cat = Category.objects.filter(status=1).order_by('sortorder')
    subcat = Subcategory.objects.filter(status=1).order_by('sortorder')
    subcat_list = {}

    for ca in cat:
        for sub in subcat:
            if sub.category == ca:

                subcat_list[ca.id] = (sub.id, sub.c_name)
                break

    return {'cat':cat,'subcat': subcat_list}


def media_globals(request):

    c_dic = {}
    c_dic['url_prefix'] = 'http://%s/' % request.META.get('HTTP_HOST')
    c_dic['url_prefix_media'] = 'http://%s%s' % (request.META.get('HTTP_HOST'), settings.MEDIA_URL)
    c_dic['url_prefix_images'] = 'http://%s%s%s/' % (request.META.get('HTTP_HOST'), settings.MEDIA_URL, 'images')
    return c_dic