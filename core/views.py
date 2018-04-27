from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from core.models import Course, Assignment, Scorecard
# Create your views here.

# Using class based views
class AssignmentStudentView(ListView):
    template_name = 'core/table.html.j2'

    def get_queryset(self):
        return Assignment.objects.order_by('display_name')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['course_name'] = self.kwargs['course_number']
    #     return context 

class ScorecardStudentView(DetailView):
    model = Scorecard
    template_name = 'core/view_scorecard.html.j2'
    context_object_name = 'scorecard'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['course_name'] = self.kwargs['course_number']
    #     return context

    #TODO look up how to create a query set in a detail view 
    # fix the urls from login
    # make sure that only people logged in can see what they have

    def get_object(self, queryset=None):
        scorecard = {
            "groups": [
                {
                    "group_name": "group 1",
                    "sections": [
                        {
                            "section_name": "BT Class",
                            "items": [
                                {
                                    "description": "Copy constructor correctly makes deep copy, handles empty-tree case",
                                    "points_max": 2,
                                    "points_received": 2
                                },
                                {
                                    "description": "Assignment operator: correctly makes a deep copy, handles empty tree case",
                                    "points_max": 2,
                                    "points_received": 2
                                }
                            ],
                            "comments": "get_height needs base case for one element tree. Average age needs to check for empty tree."
                        },

                    ]
                }
            ],
            "comments": "Great"
        }

        total_received = 0
        total_max = 0

        for section in scorecard['groups'][0]['sections']:

            section_received = 0
            section_max = 0

            for item in section['items']:
                  section_received += item['points_received']
                  section_max += item['points_max']

            section['section_received'] = section_received
            section['section_max'] = section_max

            total_received += section_received
            total_max += section_max

        scorecard['total_received'] = total_received
        scorecard['total_max'] = total_max
        scorecard['total_percentage'] = int((total_received / total_max) * 100)
        # rounding?

        return scorecard








