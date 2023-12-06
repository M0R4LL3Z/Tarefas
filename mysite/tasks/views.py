from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.mail import send_mail
from .models import Task
from .forms import Taskform

def post_list(request):
    tasks = Task.objects.all
    return render(request, 'site/tasklist.html', {'tasks': tasks})

def newtask(request):
    if request.method == 'POST':
        form = Taskform(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = Taskform()
        return render(request, 'site/addtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'site/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'site/edittask.html', {'form': form, 'task': task})

def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')

def envia_email(request):
    send_mail('Tarefas','Você tem tarefas para cuncluir','damacenag40@gmail.com',['gdamacena7@gmail.com'])
    return redirect('/')

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'site/task.html', {'task': task})

