from django.http.response import HttpResponse
from django.shortcuts import render

from django.template import context, loader
from . models import Blog

# Add post, working with forms
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . forms import AddPostForm

def blog(request):
    template = loader.get_template('blogApp/blog.html')
    bbs = Blog.objects.order_by('-date')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'blogApp/about.html')

def office(request):
    return render(request, 'blogApp/office.html')

def add(request):
    return render(request, 'blogApp/addpost.html')

class BlogCreateView(CreateView):
    template_name = 'blogApp/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.all()
        return context 