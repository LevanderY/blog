from django.conf.urls import include, url
from . import views

# Для підключення картинок з моделі
from blog import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('blog/', views.blog, name="blog"),
    url('about/', views.about, name="about"),
    url('office/', views.office, name="office"),
    url('accounts/', include('allauth.urls')),
    url('', views.log, name='log'),
]

# Для підключення картинок з моделі
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
