from django.shortcuts import render
from django.http import HttpResponse
from .models import College


def home(request):
    return render(request, "resources/base.html")


def college_list(request):
    colleges = College.objects.all()
    return render(request, "resources/college_list.html", {"colleges": colleges})


def college_page(request, college_id):
    college = College.objects.get(id=college_id)

    departments = college.departments.all()

    return render(
        request,
        "resources/college_page.html",
        {"college": college, "departments": departments},
    )
