from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("process", views.process, name="process"),
    path("new_cust", views.new_cust, name="new_cust"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("project_list", views.project_list, name="project_list"),
    path("build_input", views.build_input, name="build_input")
    ]