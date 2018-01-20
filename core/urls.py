from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html.j2'), name='login'),
    url('', include('django.contrib.auth.urls')),
    url(r'^test_endpoint/$', TemplateView.as_view(template_name='core/test.html.j2'))
]
