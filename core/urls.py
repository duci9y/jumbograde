from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url(r'^test_endpoint/$', TemplateView.as_view(template_name='core/grade.html.j2'))
]
