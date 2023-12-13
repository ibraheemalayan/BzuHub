from django.db import models


class College(models.Model):
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the college in the admin panel
    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "كلية"
        verbose_name_plural = "الكليات"

    # Type hinting
    departments: models.QuerySet["Department"]


# those are what has grey background in https://ritaj.birzeit.edu/hemis/bu/hierarchy?mode=CB
class Department(models.Model):
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, related_name="departments"
    )

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the department in the admin panel
    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "الدائرة"
        verbose_name_plural = "الدوائر"

    # Type hinting
    majors: models.QuerySet["Major"]

    # TODO related to a club/club members in the FUTURE


class Major(models.Model):
    major_code = models.CharField(
        max_length=4,
        unique=True,
        primary_key=True,
    )  # like ENCS, ARAB, ENEE, ITAL, etc...

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="majors"
    )

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the major in the admin panel
    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = "التخصص"
        verbose_name_plural = "التخصصات"

    # Type hinting
    courses: models.QuerySet["Course"]


class Course(models.Model):
    course_id = models.CharField(
        max_length=10, unique=True
    )  # full course id like ENCS101, ARAB101, ENEE2133, ITAL101, etc...

    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="courses")

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the course in the admin panel
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


class Resource(models.Model):
    title = models.CharField(max_length=64)
    #  TODO enum
    # resource_type = one of [formats,slides,books,book-solutions,lecture-notes,projects,other,homeworks]

    # TODO make it nullable
    resource_group = models.ForeignKey(
        ResourceGroup, on_delete=models.CASCADE, related_name="resources"
    )

    path: str

    is_link = models.BooleanField(default=False)

    class Meta:
        verbose_name = "مصدر"
        verbose_name_plural = "مصادر"


# TODO make courses related to departments not majors

# TODO make a secondary table for majopr-course MTM relation with field for place in advisory plan

# TODO add flag to each major `is_psuedo_major` to indicate if it's a real major or a pseudo major
