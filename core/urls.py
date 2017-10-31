from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
]
