from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from quotes.models import Quotes, Author
import re

# Create your views here.


def index1(request):
    quotesset = Quotes.objects.all()
    quotes = quotesset[:10]
    data = (q for q in quotes)
    return render(request, 'index1.html', {'data': data})


def index(request):
    quotesset = Quotes.objects.all()
    paginator = Paginator(quotesset, 10)
    try:
        quotes = paginator.page(1)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except InvalidPage:
        HttpResponse('请求的页数不存在')  # 后面添加不存在的页面，做为返回
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)  # paginator.num_pages: 总页数，此处用于最后一页
    return render(request, 'index.html', {'quotes': quotes})


def paginator_view(request, page_num):
    quotesset = Quotes.objects.all()
    paginator = Paginator(quotesset, 10)

    try:
        quotes = paginator.page(page_num)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except InvalidPage:
        HttpResponse('请求的页数不存在')  # 后面添加不存在的页面，做为返回
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)  # paginator.num_pages: 总页数，此处用于最后一页

    return render(request, 'page.html', {'quotes': quotes})


def author_view(request, authornm):
    author_info = Author.objects.get(name=authornm)
    return render(request, 'author.html', {'author': author_info})
