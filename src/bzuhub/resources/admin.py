from django.contrib import admin

from .models import College, Department, Major, Course


class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_ar")
    search_fields = ("name_en", "name_ar")


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_ar", "college")
    search_fields = ("name_en", "name_ar", "college__name_en", "college__name_ar")


class MajorAdmin(admin.ModelAdmin):
    list_display = ("major_code", "name_en", "name_ar", "department")
    search_fields = (
        "major_code",
        "name_en",
        "name_ar",
        "department__name_en",
        "department__name_ar",
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "name_en", "name_ar", "major")
    search_fields = (
        "course_id",
        "name_en",
        "name_ar",
        "major__major_code",
        "major__name_en",
        "major__name_ar",
    )


admin.site.register(College, CollegeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Course, CourseAdmin)
