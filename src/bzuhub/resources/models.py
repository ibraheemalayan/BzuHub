from django.db import models


class College(models.Model):
    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the college in the admin panel
    def __str__(self):
        return self.name_ar


# those are what has grey background in https://ritaj.birzeit.edu/hemis/bu/hierarchy?mode=CB
class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the department in the admin panel
    def __str__(self):
        return self.name_ar

    # TODO related to a club/club members in the FUTURE


class Major(models.Model):
    major_code = models.CharField(
        max_length=4,
        unique=True,
        primary_key=True,
    )  # like ENCS, ARAB, ENEE, ITAL, etc...

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the major in the admin panel
    def __str__(self):
        return self.name_ar


class Course(models.Model):
    course_id = models.CharField(
        max_length=10, unique=True
    )  # full course id like ENCS101, ARAB101, ENEE2133, ITAL101, etc...

    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    name_en = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64)

    # used to represent the course in the admin panel
    def __str__(self):
        return self.course_id + " " + self.name_en
