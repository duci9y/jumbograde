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

class ScorecardTemplateInline(admin.TabularInline):
    model = models.ScorecardTemplate

class AssignmentAdmin(admin.ModelAdmin):
    inlines = [
        ScorecardTemplateInline,
    ]
    
    list_display = ('display_name', 'due_date', 'scorecards_published', 'is_published',
                    'accepting_submissions',)




class CourseAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'course_number', 'semester', 'default_extensions',
                    'default_max_extensions', 'is_active',)



admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Assignment, AssignmentAdmin)
admin.site.register(models.Course, CourseAdmin)
