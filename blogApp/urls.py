from os import name
from django.conf.urls import include, url
from django.urls import path
from . import views

# Для підключення картинок з моделі
from blog import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# For adding post
from . views import BlogCreateView

urlpatterns = [
    path('', views.about),
    url('blog/', views.blog, name='blog'),
    url('about/', views.about, name='about'),
    url('office/', views.office, name='office'),
    url('add/', BlogCreateView.as_view(), name='add'),
    url('accounts/', include('allauth.urls')),
]

# Для підключення картинок з моделі
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
