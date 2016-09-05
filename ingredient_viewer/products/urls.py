from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import list_all

urlpatterns = [
    url(r'^overview', list_all, name='list_all'),
    url(r'^$', list_all, name='list_all'),
]
