from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from. forms import TaskForm
from . models import Task
from django.utils import timezone

def home(request):
    return render(request, 'habitica/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'habitica/signupuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenthabits')
            except IntegrityError:
                return render(request, 'habitica/signupuser.html', {'form':UserCreationForm(), 'error':'Username exists..Please try another'})
        else:
            return render(request, 'habitica/signupuser.html', {'form':UserCreationForm(), 'error':'Password doesnot match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'habitica/loginuser.html', {'form':AuthenticationForm()})
    else:
        #logging in a new user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'habitica/loginuser.html', {'form':AuthenticationForm(), 'error':'User is not associated with any Habitica account'} )
        else:
            login(request, user)
            return redirect('currenttasks')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def createtask(request):
    if request.method == 'GET':
        return render(request, 'habitica/createtask.html', {'form':TaskForm()})
    else:
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'habitica/createtask.html', {'form':TaskForm(), 'error':'Bad Request :( '})

def viewtask(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'habitica/viewtask.html', {'task':task, 'form':form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'habitica/viewtask.html', {'task':task, 'form':form, 'error':'Bad Request :( '})

def completetask(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('currenttasks')

def deletetask(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('currenttasks')

def completedtask(request):
    tasks = Task.objects.filter(user=request.user,  datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'habitica/completedtask.html', {'tasks':tasks})

def currenttasks(request):
    tasks = Task.objects.filter(user=request.user,  datecompleted__isnull=True)
    return render(request, 'habitica/currenttasks.html', {'tasks':tasks})
