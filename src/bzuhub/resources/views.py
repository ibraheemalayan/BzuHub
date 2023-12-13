from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import College


class HomeView(View):
    def get(self, request):
        return render(request, "resources/base.html")


class CollegeListView(View):
    def get(self, request):
        colleges = College.objects.all()
        return render(request, "resources/college_list.html", {"colleges": colleges})


class CollegePageView(View):
    def get(self, request, college_id):
        college = College.objects.get(id=college_id)
        departments = college.departments.all()
        return render(
            request,
            "resources/college_page.html",
            {"college": college, "departments": departments},
        )
