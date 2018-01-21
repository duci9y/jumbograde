from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core.views import GradeView
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html.j2'), name='login'),
    url('', include('django.contrib.auth.urls')),
    url(r'^test_endpoint/$', TemplateView.as_view(template_name='core/test.html.j2')),
    url('grade/', GradeView.as_view())
]
