from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .forms import *
from .utils import calculate_priority
from django.contrib.auth import logout


# Create your views here.
# views.py
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home') 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


@login_required
def home(request):
    high = Task_highform()
    context ={
        'form':high
    }
    return render(request, 'home.html')

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.ai_priority_score = calculate_priority(task)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('ai_priority_score')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


def task_high(request):
    if request.method == 'POST':
        form = Task_highform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assuming Task_high has a user field
            task.ai_priority_score = calculate_priority(task)  # Assuming you have this function
            task.save()
            return redirect('task_high_list')
    else:
        form = Task_highform()

    context = {
        'form': form
    }
    return render(request, 'highpri.html', context)

def task_high_list(request):
    tasks = Task_high.objects.filter(user=request.user).order_by('-due_date')
    return render(request, 'highpri_list.html', {'tasks': tasks})

def task_high_update(request, pk):
    task = Task_high.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = Task_highform(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.ai_priority_score = calculate_priority(task)
            task.save()
            return redirect('task_high_list')
    else:
        form = Task_highform(instance=task)
    return render(request, 'highpri_update.html', {'form': form})


def task_high_delete(request, pk):
    task = get_object_or_404(Task_high, id=pk, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_high_list')  # Adjust to your list view name

    return render(request, 'highpri_delete.html', {'task': task})


def task_medium(request):
    if request.method == 'POST':
        form = Task_mediumform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Make sure Task_medium has a user field
            task.ai_priority_score = calculate_priority(task)  # Optional AI score
            task.save()
            return redirect('task_medium_list')
    else:
        form = Task_mediumform()

    context = {
        'form': form
    }
    return render(request, 'medium.html', context)

from django.core.paginator import Paginator

def task_medium_list(request):
    task_list = Task_medium.objects.filter(user=request.user).order_by('-due_date')
    paginator = Paginator(task_list, 5)  # Show 5 tasks per page

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'medium_list.html', {'tasks': tasks})

def task_medium_update(request, pk):
    task = Task_medium.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = Task_mediumform(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.ai_priority_score = calculate_priority(task)
            task.save()
            return redirect('task_medium_list')
    else:
        form = Task_mediumform(instance=task)

    return render(request, 'medium_update.html', {'form': form})

def task_medium_delete(request, pk):
    task = Task_medium.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_medium_list')
    return render(request, 'medium_delete.html', {'task': task})


def task_delow(request):
    if request.method == 'POST':
        form = Task_lowform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.ai_priority_score = calculate_priority(task)  # Optional
            task.save()
            return redirect('low') 
    else:
        form = Task_lowform()

    tasks = Task_low.objects.filter(user=request.user).order_by('-due_date')
    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'low.html', context)

def task_delowt(request):
    tasks = Task_low.objects.filter(user=request.user).order_by('-due_date')
    return render(request, 'low.html', {'tasks': tasks})

@login_required
def edit_low_task(request, pk):
    task = get_object_or_404(Task_low, pk=pk, user=request.user)
    if request.method == 'POST':
        form = Task_lowform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('low')
    else:
        form = Task_lowform(instance=task)
    return render(request, 'edit_low_task.html', {'form': form})


@login_required
def delete_low_task(request, pk):
    task = get_object_or_404(Task_low, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('low')
    return render(request, 'delete_low_task.html', {'task': task})
