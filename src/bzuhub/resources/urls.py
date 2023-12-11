from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("colleges/", views.college_list, name="college_list"),
    path("colleges/<int:college_id>/", views.college_page, name="college_page"),
]
