from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from core.models import Course, Assignment

# Using class based views
class CourseList(ListView):
    template_name = 'core/courses.html.j2'

    def get_queryset(self):
        return Course.objects.order_by('course_number')

class AssignmentList(ListView):
    template_name = 'core/assignments.html.j2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_name'] = self.kwargs['course_number']
        return context

    def get_queryset(self):
        return Assignment.objects.order_by('display_name')
