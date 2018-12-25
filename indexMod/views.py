from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.http import StreamingHttpResponse


def index(request):
    '''
    index 首页
    :param request:
    :return:
    '''
    return render(request, 'index/index.html')
