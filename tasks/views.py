from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm, EditTaskForm

def dashboard(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'tasks/dashboard.html', { 'tasks': tasks })

    return redirect('/authentication/login/')

def add_task(request):
    if request.user.is_authenticated:
        form = TaskForm(data={'user': request.user, 'completed': False})

        if request.method == 'POST':
            form = TaskForm(data=request.POST)

            if form.is_valid():
                task = form.save()
                messages.success(request, f'The task {task.name} was added successfully!')
                return redirect('/')

        return render(request, 'tasks/add_task.html', { 'form': form })

    return redirect('/authentication/login/')

def update_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, pk=pk)
        form = EditTaskForm(instance=task)

        if request.method == 'POST':
            form = EditTaskForm(instance=task, data=request.POST)

            if form.is_valid():
                task = form.save()
                messages.success(request, f'The task was updated successfully!')
                return redirect('/')

        return render(request, 'tasks/update_task.html', { 'form': form })

    return redirect('/authentication/login/')

def remove_task(request, pk):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        messages.success(request, f'The task was removed successfully!')
        return redirect('/')

    return redirect('/authentication/login/')
