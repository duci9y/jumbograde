from django.shortcuts import render
from django.views import View

from .models import Scorecard
from .models import Assignment

# Create your views here.
class GradeView(View):
        def get(self, request):
                assignment_list = Assignment.objects.order_by('display_name')
                context = {
                        'assignment_list' : assignment_list,
                }
                return render(request, 'core/grade.html.j2', context)