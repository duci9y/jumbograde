from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url(r'^test_endpoint/$', TemplateView.as_view(template_name='core/test.html.j2')),
    url(r'^grading/$', TemplateView.as_view(template_name='core/grade.html.j2')),
    url(r'^student/$', TemplateView.as_view(template_name='core/table.html.j2')),
    url(r'^login/$', TemplateView.as_view(template_name='core/login.html.j2'))
]
