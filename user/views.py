from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
import django.contrib.auth as auth
from .forms import LoginForm, RegisterForm


@require_http_methods(["GET", "POST"])
def login(request: HttpRequest) -> HttpResponse:
    form: LoginForm

    if request.method == "GET":
        form = LoginForm()

    else:  # POST
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                request,
                username=form.data.get("username"),
                password=form.data.get("password"),
            )
            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "User not found.")

    return render(request, "login.html", {"form": form})


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    form: RegisterForm

    if request.method == "GET":
        form = RegisterForm()

    else:  # POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "register.html", {"form": form})


@require_http_methods(["POST"])
def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect("login")
