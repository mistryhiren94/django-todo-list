from django.shortcuts import render,HttpResponse,redirect
from . models import Todo
from django.http import JsonResponse

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

def updateTodo(request, id):
    if request.method == "GET":
        todo = Todo.objects.get(id = id)
        context = {
            "todo":todo
        }
        return render(request, "update.html", context)
    elif request.method == "POST":
        text = request.POST.get('todo')
        print(text)
        Todo.objects.filter(id=id).update(text=text)
        # return JsonResponse({
        #     'data':'Updated'
        # })
        return redirect('/')
