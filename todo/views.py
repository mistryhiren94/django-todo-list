from django.shortcuts import render,HttpResponse,redirect
from . models import Todo

# Create your views here.

def index(request):
    todo = Todo.objects.all()
    context = {
        "todo":todo
    }
    return render(request, "index.html", context)

def saveTodo(request):
    text = request.POST.get('todo')
    Todo.objects.create(text = text)
    return redirect('/')

def removeTodo(request, id):
    deleteTodo = Todo.objects.get(id = id)
    deleteTodo.delete()
    return redirect('/')
