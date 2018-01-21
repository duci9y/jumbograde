from django.shortcuts import render
from django.http import HttpResponse
from core.models import Assignment 
# Create your views here.

def get_assignments(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    assignment_list = Assignment.objects.order_by('-due_date')[:5]
    context_dict = {'assignments': assignment_list}

    # Render the response and send it back!
    return render_to_response('core/courses.html.j2', context_dict, context)


