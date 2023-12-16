from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_user),
    path('success/', views.render_success),
    path('logout/', views.log_out),
    path('login/', views.log_in),
    path('delete_all/', views.delete_all),
]