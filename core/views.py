from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from core.models import Course, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

# Using class based views
class CourseList(LoginRequiredMixin, ListView):
    template_name = 'core/courses.html.j2'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


    def get_queryset(self):
        user_groups = self.request.user.groups.values_list('id', flat=True)
        return Course.objects.filter(grader_posix_group__in=user_groups)

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

    def dispatch(self, request, *args, **kwargs):
        course = get_object_or_404(Course, course_number=self.kwargs['course_number'])

        if course.grader_posix_group not in self.request.user.groups.all():
            return redirect(reverse('course_list'))
        return super(AssignmentList, self).dispatch(request, *args, **kwargs)
