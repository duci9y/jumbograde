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

class ScorecardStudentView(View):
     def get(self, request):
        scorecard = [
                {
                        "group_name": "group1",
                        "sections": [
                            {
                                "section_name": "Part 1",
                                "items": [
                                    {
                                        "description": "Does this",
                                        "points_max": 4,
                                        "points_received": 4
                                    }
                                ],
                                "comments": "good job"
                            },
                            {
                                "section_name": "Part 2",
                                "items": [
                                    {
                                        "description": "does that",
                                        "points_max": 10,
                                        "points_received": 5
                                    }
                                ],
                                "comments": "you missed the part where you did that thing"
                            },
                             {
                                "section_name": "Part 3",
                                "items": [
                                    {
                                        "description": "does everything",
                                        "points_max": 6,
                                        "points_received": 6
                                    }
                                ],
                                "comments": "wow!"
                            }

                        ],
                        
                },
        ]
        context = {
            'scorecard' : scorecard,
        }
        return render(request, 'core/view_scorecard.html.j2', context) 







