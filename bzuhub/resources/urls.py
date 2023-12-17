from django.urls import path

from . import views

from .views import HomeView, CollegeListView, CollegePageView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("colleges/", CollegeListView.as_view(), name="college_list"),
    path("colleges/<int:college_id>/", CollegePageView.as_view(), name="college_page"),
]
