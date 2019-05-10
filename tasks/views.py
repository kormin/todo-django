from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from tasks.models import Tasks


def index(request):
    tasks = Tasks.objects.all()
    return render(
        request, 'index.html',
        context={'tasks': tasks},
    )


def add_task(request):
    if request.method == 'POST':
        Tasks.objects.create(name=request.POST.get('task'))
        return redirect('index')
    return render(request, 'tasks_fail.html')


def edit_task(request, id):
    task = get_object_or_404(Tasks, pk = id)
    if request.method == 'POST':
        task.name = request.POST.get('task')
        task.save()
        return redirect('index')
    return render(
        request, 'tasks_edit.html',
        context={'task': task},
    )


def delete_task(request, id):
    task = get_object_or_404(Tasks, pk = id)
    task.delete()
    return redirect('index')


def toggle_task(request, id):
    task = get_object_or_404(Tasks, pk = id)
    if not task.is_done:
        task.is_done = True
    else:
        task.is_done = False
    task.save()
    return redirect('index')
