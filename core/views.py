from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from core.models import Course, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin

# Using class based views
class CourseList(LoginRequiredMixin, ListView):
    template_name = 'core/courses.html.j2'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        #return Course.objects.filter(course__grader_posix_group=)
        print(self.kwargs)
        return Course.objects.order_by('course_number')

class AssignmentList(LoginRequiredMixin, ListView):
    template_name = 'core/assignments.html.j2'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_name'] = self.kwargs['course_number']
        return context

    def get_queryset(self):
        return Assignment.objects.filter(course__course_number=self.kwargs['course_number']).order_by('display_name')
