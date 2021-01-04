from django import template
from django.http.response import HttpResponse
from django.shortcuts import render

from django.template import context, loader
from . models import Blog

def main(request):
    template = loader.get_template('blogApp/mainPage.html')
    bbs = Blog.objects.order_by('date')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'blogApp/about.html')

def office(request):
    return render(request, 'blogApp/office.html')
