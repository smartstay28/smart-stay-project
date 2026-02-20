from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib import messages


def select_role(request):
    return render(request, "select_role.html")


def register_view(request):
    role = request.GET.get("role") or request.POST.get("role")

    if request.method == "POST":
        username = request.POST["username"]
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        aadhar = request.POST["aadhar"]
        contact = request.POST["contact"]
        birthdate = request.POST["birthdate"]
        password = request.POST["password"]
        occupation = request.POST["occupation"]
        address = request.POST["address"]

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "registration.html", {"error": "Username already exists", "role": role})
         
         # Aadhar number unique check
        if CustomUser.objects.filter(aadhar_number=aadhar).exists():
            return render(request, "registration.html", {"error": "Aadhar number already registered!", "role": role})

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        user.full_name = fullname
        user.aadhar_number = aadhar
        user.contact_number = contact
        user.birth_date = birthdate
        user.occupation = occupation
        user.address = address
        user.role = role
        user.save()

        return redirect("login")

    return render(request, "registration.html", {"role": role})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("welcome")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")

@login_required
def welcome(request):
    return render(request, "welcome.html", {
        "username": request.user.username,
        "role": request.user.role
    })

def logout_view(request):
    logout(request)
    return redirect("login")


# def register_view(request):
#     if request.method == "POST":
#         aadhar = request.POST.get("aadhar")

#         if CustomUser.objects.filter(aadhar_number=aadhar).exists():
#             messages.error(request, "Aadhar number already registered!")
#             return redirect("register")

#         # then create user