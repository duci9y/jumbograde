from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core.views import CourseList, AssignmentList, ScorecardRedirectView, ScorecardView

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html.j2'), name='login'),
    url('', include('django.contrib.auth.urls')),
    url(r'^grade/$', CourseList.as_view(), name='course_list'),
    url(r'^grade/(?P<course_number>[a-zA-Z0-9\s]+)/$', AssignmentList.as_view(), name='assignment_list'),
    url(r'^grade/(?P<course_number>[a-zA-Z0-9\s]+)/(?P<assignment_name>[a-zA-Z0-9\s]+)/$', ScorecardRedirectView.as_view(), name='scoring_view'),
    url(r'^grade/(?P<course_number>[a-zA-Z0-9\s]+)/(?P<assignment_name>[a-zA-Z0-9\s]+)/(?P<scorecard_id>[a-z0-9]{8,})/$', ScorecardView.as_view(), name='scorecard-detail'),
]
