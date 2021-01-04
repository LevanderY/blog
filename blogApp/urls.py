from django.conf.urls import url
from . import views
# from blogApp.models import Blog

# Для підключення картинок з моделі
from blog import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('main/', views.main, name="main"),
    url('about/', views.about, name="about"),
    url('office/', views.office, name="office"),
]

# Для підключення картинок з моделі
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
