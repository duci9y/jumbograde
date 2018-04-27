from celery import shared_task
from core.models import Course, Assignment, Submission, Student
from django.conf import settings
import os

@shared_task
def poll_for_new_submissions():
    courses = Course.objects.all()

    for course in courses:
        assignments = Assignment.objects.filter(course=course)

        for assignment in assignments:
            path = os.path.join(settings.SUBMISSION_DIR,
                                course.course_number,
                                course.semester,
                                'grading',
                                assignment.display_name)

            print('Reading path ' + path)

            submission_dirs = next(os.walk(path), [None, []])[1]

            print('Reading assignment at ' + str(submission_dirs))

            for dir_name in submission_dirs:
                # check if any submission exists in db
                # if yes, check if versions match
                #   if yes, do nothing
                #   if not, update version number
                # if not, add submission to db
                username, version = dir_name.split('.')

                if Submission.objects.filter(assignment=assignment,
                                             student__user__username=username).exists():
                    submission = Submission.objects.get(assignment=assignment,
                                                        student__user__username=username)

                    if version > submission.latest_version:
                        submission.latest_version = version
                        submission.path = os.path.join(path, dir_name)
                        submission.save()
                else:
                    submission = Submission()
                    submission.student = Student.objects.get(user__username=username)
                    submission.assignment = assignment
                    submission.latest_version = version
                    submission.path = os.path.join(path, dir_name)
                    submission.save()