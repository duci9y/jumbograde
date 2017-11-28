from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

class TimestampsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(models.Model):
    display_name = models.CharField(max_length=32)
    course_number = models.CharField(max_length=16)
    semester = models.CharField(max_length=32)
    default_extensions = models.PositiveSmallIntegerField(default=0)
    default_max_extensions = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=32)
    courses_active = models.ManyToManyField(Course, related_name='students')
    courses_grading = models.ManyToManyField(Course, related_name='graders')
    courses_dropped = models.ManyToManyField(Course, related_name='dropped_students')


class ScorecardFormat(models.Model):
    # TODO: Think more
    data = JSONField()


class Autograder(models.Model):
    display_name = models.CharField(max_length=100)
    description = models.TextField()
    invocation = models.CharField(max_length=100)
    archive = models.FileField(upload_to='autograders/')


class Assignment(models.Model):
    display_name = models.CharField(max_length=32)
    scorecard_format = models.OneToOneField(ScorecardFormat, on_delete=models.CASCADE)
    autograders = models.ManyToManyField(Autograder, related_name='assignments')
    due_date = models.DateTimeField()
    scorecards_published = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    max_extensions = models.PositiveSmallIntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    accepting_submissions = models.BooleanField(default=False)


class Extension(models.Model):
    initial = models.PositiveSmallIntegerField(default=0)
    remaining = models.PositiveSmallIntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='extensions')


class Scorecard(TimestampsModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scorecards_received')
    grader = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scorecards_graded')
    data = JSONField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='scorecards')


class Submission(TimestampsModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    # is_late 
    latest_version = models.PositiveSmallIntegerField(default=0)
    # TODO: Figure out if this is ok
    path = models.CharField(max_length=100)


class Event(TimestampsModel):
    title = models.CharField(max_length=140)
    message = models.TextField()
    course = models.ForeignKey(Course, blank=True, on_delete=models.CASCADE)
    # severity?
