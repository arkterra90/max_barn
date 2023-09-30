from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_cust", views.new_cust, name="new_cust"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("project_list", views.project_list, name="project_list"),
    path("build_input", views.build_input, name="build_input"),
    path("user_admin", views.user_admin, name="user_admin"),
    path("admin_contacts", views.admin_contacts, name="admin_contacts"),
    path("<int:cust_id>/customer_details", views.customer_details, name="customer_details"),
    path("<int:cust_id>/customer_profile", views.customer_profile, name="customer_profile"),
    path("customer_list", views.customer_list, name="customer_list"),
    path("note_add", views.note_add, name="note_add")
    ]