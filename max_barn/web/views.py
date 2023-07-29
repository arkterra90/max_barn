from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . forms import *

# Create your views here.
def index(request):
    return render(request, "web/index.html")

def about(request):
    return render(request, "web/about.html")

def process(request):
    return render(request, "web/process.html")

def user_admin(request):
    return render(request, "web/user_admin.html")

def admin_contacts(request):
    contacts = Customer.objects.all()
    print(contacts)

    return render(request, "web/admin_contacts.html", {
        "contacts": contacts
    })

def new_cust(request):
    if request.method == "POST":
        f = CustomerForm(request.POST)
        if f.is_valid():
            instance = f.save()
            return render(request, "web/contact.html", {
                "message": "Thank you for submitting your contact information! A representative will contact you soon.",
                "CustomerForm": CustomerForm
            })
        else:
            print(f.errors)
            return render(request, "web/contact.html", {
            "CustomerForm": CustomerForm,
            "message": "Your information was not saved. Please try again."
            })
    else:
        return render(request, "web/contact.html", {
            "CustomerForm": CustomerForm
        })
    
def project_list(request):
    user_project = request.user.project
    project = Item.objects.filter(building=user_project)
    return render(request, "web/client_project.html", {
        "project": project
    })

def build_input(request):
    if request.method == "POST":
        f = BuildingForm(request.POST)
        if f.is_valid():
            instance = f.save()
            return render(request, "web/build_input.html", {
                "message": "Saved",
                "BuildingForm": BuildingForm
            })
    else:
        return render(request, "web/build_input.html", {
            "BuildingForm": BuildingForm
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "web/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "web/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Registers a new user.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "web/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "web/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "web/register.html")