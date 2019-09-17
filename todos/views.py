from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()[:10]

    form = TodoForm()

    context = {'todos': todos, 'form': form}

    return render(request, 'index.html', context)

@require_POST
def add(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo(text = request.POST['text'])
        todo.save()

        return redirect('index')


def completeTodo(request, id):
    todo = Todo.objects.get(pk=id)
    todo.is_complete=True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(is_complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')