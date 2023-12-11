from django.contrib import admin

from .models import College, Department, Major, Course

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Course)
