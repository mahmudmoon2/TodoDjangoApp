from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from . forms import ToDoForm
from . models import Task
from django.db import models

# Create your views here.
@login_required
def home(request):
    tasks = Task.objects.filter(created_by = request.user)
    status = request.GET.get('status')
    if status == 'completed':
        tasks = tasks.filter(is_completed = True)
    elif status == 'remaining':
        tasks = tasks.filter (is_completed = False)
        
    search = request.GET.get('search')
    if search :
        tasks = tasks.filter(
            models.Q(title__icontains = search) | models.Q(description__icontains = search))    
    return render(request, 'index.html' , {'tasks': tasks})
# task details
@login_required
def task_detail (request, task_id):
    task = Task.objects.get(pk = task_id, created_by = request.user)
    return render(request, 'task_detail.html' , {'task': task})
# delete
@login_required
def task_delete (request, task_id):
    task = Task.objects.get(pk = task_id, created_by = request.user)
    task.delete()
    return redirect('/')


# This is register view

def register (request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request,user)
            return redirect ('/')
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html' , {'form' : form})

# Login view

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render (request, 'login.html' , {'form' : form})

#Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#create
@login_required
def task_create (request):
    if request.method =='POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect ('/')
    else:
        form = ToDoForm()
        
    return render(request, 'create_todo.html' , {'form' : form})

#toggle
@login_required
def toggle_task_status(request, task_id):
    task = Task.objects.get(pk = task_id, created_by = request.user)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
        
    task.save()   
    return redirect(request.META.get('HTTP_REFERER', 'home'))