from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm


@login_required(login_url="user/login/")
@require_http_methods(["GET"])
def home(request: HttpRequest) -> HttpResponse:
    task = Task.objects.filter(owner=request.user)
    paginator = Paginator(task, 4)
    page_number = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        "expense": task,
        "page_obj": page_obj,
    }
    return render(request, "home.html", context)


@require_http_methods(["GET", "POST"])
def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = TaskForm()

    else:  # POST
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")

    return render(request, "add-task.html", {"form": form})


@require_http_methods(["GET", "POST"])
def edit_task(request: HttpRequest, pk) -> HttpResponse:
    instance = get_object_or_404(Task, pk=pk)

    if request.method == "GET":
        form = TaskForm()

    else:  # POST
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "edit_task.html", {"form": form, "pk": pk})


@require_http_methods(["GET"])
def delete_task(request: HttpRequest, pk) -> HttpResponse:
    instance = get_object_or_404(Task, pk=pk)
    instance.delete()
    return redirect("home")


@require_http_methods(["GET"])
def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
