from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import django.contrib.auth as auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        response: HttpResponse
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                request,
                username=form.data.get("username"),
                password=form.data.get("password"),
            )
            if user is not None:
                auth.login(request, user)
                response = HttpResponse("Logged")
            else:
                response = HttpResponse("User not found")
        else:
            response = HttpResponse("Form is invalid")
        return response


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":
        response: HttpResponse
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.data.get("username")
            email = form.data.get("email")
            if not user_exists(username, email):
                new_user = User.objects.create_user(
                    username=username, password=form.data.get("password"), email=email
                )
                response = HttpResponse("Registered")
            else:
                response = HttpResponse("Username or Email already registered")
        else:
            response = HttpResponse("Form is invalid")
        return response


def user_exists(username, email):
    return (
        User.objects.filter(username=username).exists()
        or User.objects.filter(email=email).exists()
    )
