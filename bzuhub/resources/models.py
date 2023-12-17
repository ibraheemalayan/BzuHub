from django.db import models
from django.utils.translation import gettext_lazy as _


# those are what has [Green background] in https://ritaj.birzeit.edu/hemis/bu/hierarchy?mode=CB
class College(models.Model):
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "كلية"
        verbose_name_plural = "الكليات"


# those are what has [Bold Grey background] in https://ritaj.birzeit.edu/hemis/bu/hierarchy?mode=CB
class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="departments")
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "الدائرة"
        verbose_name_plural = "الدوائر"

    # TODO related to a club/club members in the FUTURE


# those are what has [Grey background] in https://ritaj.birzeit.edu/hemis/bu/hierarchy?mode=CB
class Major(models.Model):
    major_code = models.CharField(max_length=4, unique=True, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="majors")
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)
    is_pseudo_major = models.BooleanField(default=False)  # Flag for pseudo major

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "التخصص"
        verbose_name_plural = "التخصصات"


class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True) # full course id like ENCS101, ARAB101, ENEE2133, etc...
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses", null=True)
    majors = models.ManyToManyField(Major, related_name="courses", blank=True)

    def __str__(self):
        return self.course_id + " " + self.name_en

    class Meta:
        verbose_name = "المساق"
        verbose_name_plural = "المساقات"


# quizes, exams, homeworks, etc...
class ResourceGroup(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="resource_groups"
    )


class ResourceType(models.TextChoices):
    FORMATS = 'formats', _('Formats')
    SLIDES = 'slides', _('Slides')
    BOOKS = 'books', _('Books')
    BOOK_SOLUTIONS = 'book-solutions', _('Book Solutions')
    LECTURE_NOTES = 'lecture-notes', _('Lecture Notes')
    PROJECTS = 'projects', _('Projects')
    OTHER = 'other', _('Other')
    HOMEWORKS = 'homeworks', _('Homeworks')


class Resource(models.Model):
    title = models.CharField(max_length=64)
    resource_group = models.ForeignKey(
        ResourceGroup, on_delete=models.CASCADE, related_name="resources"
    )
    resource_type = models.CharField(
        max_length=20,
        choices=ResourceType.choices,
        null=True,  # Making the field nullable
        blank=True  # Allows the field to be blank in forms
    )
    is_link = models.BooleanField(default=False)

    class Meta:
        verbose_name = "مصدر"
        verbose_name_plural = "مصادر"


# TODO make courses related to departments not majors [Done]

# TODO add flag to each major `is_psuedo_major` to indicate if it's a real major or a pseudo major  [Done]

# TODO make a secondary table for majopr-course MTM relation with field for place in advisory plan

