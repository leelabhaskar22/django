from django.urls import URLPattern, path

from . import views
from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView
urlpatterns =[
    path('',views.home, name='home'),
    path('year',views.year, name='year'),
    path('year', views.month ,name='month'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico')))


]
