from django.contrib import admin
from . import models

class StudentAdmin(admin.ModelAdmin):
    def first_name(self, instance):
        return instance.user.first_name

    def last_name(self, instance):
        return instance.user.last_name

    def username(self, instance):
        return instance.user.username

    list_display = ('username', 'preferred_name', 'first_name', 'last_name',)

admin.site.register(models.Student, StudentAdmin)
