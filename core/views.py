from django.shortcuts import render
from django.views import View
from core.models import Assignment 
# Create your views here.

# Using class based views
class AssignmentStudentView(View):
    def get(self, request):
        assignment_list = Assignment.objects.order_by('display_name')
        context = {
            'assignment_list' : assignment_list,
        }
        return render(request, 'core/table.html.j2', context) 






