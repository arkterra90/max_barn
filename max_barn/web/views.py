from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . forms import *

# Renders home page.
def index(request):
    return render(request, "web/index.html")

# Renders about page.
def about(request):
    return render(request, "web/about.html")

# Renders a page with table of all potential customers who have not had
# a successful first contact.
def admin_contacts(request):
    contacts = Customer.objects.exclude(contact__isnull=False)

    return render(request, "web/admin_contacts.html", {
        "contacts": contacts
    })

# Renders building input form for admin use.
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

# Renders customer details page in first contact admin workflow.
def customer_details(request, cust_id):
    if request.method == "POST":
        customer = Customer.objects.get(pk=cust_id)
        f = ContactForm(request.POST)
        g = CustomerNoteForm(request.POST)
        print(f, g)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.cust = customer
            instance.on_site_appointment = request.POST.get('on_site_appointment')
            instance.possible_build_date = request.POST.get('possible_build_date')
            instance.save()
        if g.is_valid():
            instance = g.save(commit=False)
            instance.cust = customer
            instance.save()
        cust = Customer.objects.filter(pk=cust_id)
        return render(request, "web/customer_details.html", {
            "cust": cust,
            "contact": ContactForm,
            "cust_note": CustomerNoteForm
        })
        
    else:
        cust = Customer.objects.filter(pk=cust_id)
        return render(request, "web/customer_details.html", {
            "cust": cust,
            "contact": ContactForm,
            "cust_note": CustomerNoteForm
        })

# Returns page for entire active customer list.
def customer_list(request):
    customers = Customer.objects.all()

    return render(request, "web/customer_list.html", {
        "customers": customers
    })

def customer_profile(request, cust_id):
    customer = Customer.objects.get(pk=cust_id)
    notes = CustomerNote.objects.filter(cust=customer)
    builds = Building.objects.filter(cust=customer)
    contact = Contact.objects.filter(cust=customer)

    return render(request, "web/customer_profile.html", {
        "customers": [customer],
        "notes": notes,
        "builds": builds,
        "contacts": contact,
        "customernoteform": CustomerNoteForm
    })

# Renders customer contact form.
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
            return render(request, "web/contact.html", {
            "CustomerForm": CustomerForm,
            "message": "Your information was not saved. Please try again."
            })
    else:
        return render(request, "web/contact.html", {
            "CustomerForm": CustomerForm
        })

# Adds note to customer profile.
def note_add(request):
    cust_id = request.POST.get('cust_id')
    customer = Customer.objects.get(pk=cust_id)
    f = CustomerNoteForm(request.POST)
    if f.is_valid:
        instance = f.save(commit=False)
        instance.cust = customer
        instance.save()
    return redirect('customer_profile', cust_id=cust_id)


# Renders building process explanation page.
def process(request):
    return render(request, "web/process.html")

# Renders admin page with links to business processes.
def user_admin(request):
    return render(request, "web/user_admin.html")
    
# Currently not functional
def project_list(request):
    user_project = request.user.project
    project = Item.objects.filter(building=user_project)
    return render(request, "web/client_project.html", {
        "project": project
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