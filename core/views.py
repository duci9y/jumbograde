from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from core.models import Course, Assignment, Scorecard, Submission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

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

class ScorecardRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        # Steps:
        # - See if there are any unfinished scorecards by this grader
        # - If not, see if there are students left to be graded
        # - If yes, create new scorecard and return
        # - If not, done! redirect to... done...?
        assignment = get_object_or_404(Assignment, display_name=kwargs.get('assignment_name'))

        unfinished_set = Scorecard.objects.filter(grader=self.request.user.student,
                                                  submission__assignment=assignment,
                                                  is_done=False)
        
        ungraded_set = Submission.objects.filter(assignment=assignment,
                                                 scorecard=None)

        if unfinished_set.count() > 0:
            return pick_unfinished(unfinished_set)
        elif ungraded_set.count() > 0:
            # TODO: RACE CONDITION? multiple queries?
            return pick_ungraded(ungraded_set)
        else:
            return 'google.com'

    def pick_unfinished(unfinished_set):
        scorecard = unfinished_set.first()
        return reverse('scorecard-detail', **kwargs, scorecard_id=scorecard.id)

    def pick_ungraded(ungraded_set):
        submission = ungraded_set.all()[rand() % ungraded_set.count()]

        scorecard = Scorecard()
        scorecard.grader = self.request.user
        scorecard.submission = submission
        scorecard.data = assignment.scorecard_template.data
        scorecard.save()

        return reverse('scorecard-detail', **kwargs, scorecard_id=scorecard.id)
