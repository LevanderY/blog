from django import template
from django.http.response import HttpResponse
from django.shortcuts import render

from django.template import context, loader
from . models import Blog

def blog(request):
    template = loader.get_template('blogApp/blog.html')
    bbs = Blog.objects.order_by('date')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'blogApp/about.html')

def office(request):
    return render(request, 'blogApp/office.html')

def log(request):
    return render(request, 'account/login.html')