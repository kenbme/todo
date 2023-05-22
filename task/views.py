from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Category
from django.contrib import messages
from django.utils.timezone import now
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='user/login/')
def home(request):
    task = Task.objects.filter(owner=request.user)
    paginator = Paginator(task, 4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'expense': task,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)

def add_tasks(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'add-tasks.html', context)

    if request.method == 'POST':
        task = request.POST['name']
        description = request.POST['description']
        if request.POST['task_date'] != "":
            date = request.POST['task_date']
        else:
            date = now()
        category = request.POST['category']
        if not task:
            messages.error(request, 'Task is required')

        Task.objects.create(owner=request.user, task=task, date=date, description=description, category=category)

        return redirect('home')


def task_edit(request, id):
    categories = Category.objects.all()
    task = Task.objects.get(pk=id)
    context = {
        'expense': task,
        'values': task,
        'categories': categories
    }
    if request.method == 'GET':
        messages.info(request, 'Handling post form')
        return render(request, 'edit_task.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        description = request.POST['description']
        if request.POST['expense_date'] != "":
            date = request.POST['expense_date']
        else:
            date = now()
        category = request.POST['category']
        if not amount:
            messages.error(request, 'Amount is required')

        task.owner = request.user
        task.amount = amount
        task.date = date
        task.description = description
        task.category = category

        task.save()

        return redirect('home')


def about(request):
    return render(request, "about.html")
