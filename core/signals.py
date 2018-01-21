from django.dispatch import receiver
from django_auth_ldap.backend import populate_user
from .models import Student

@receiver(populate_user)
def create_student_for_user(sender, **kwargs):
    user = kwargs.get('user')
    s = None

    try:
        s = Student.objects.get(user=user)
    except Student.DoesNotExist as e:
        print('creating student for user')

    if not s:
        s = Student(user=user, preferred_name=user.first_name)
        s.save()

    print(s)
