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
    user = request.user
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

        # using update query
        # Todo.objects.filter(id=id).update(text=text)

        # using save function
        selectedTodo = Todo.objects.get(id = id)
        selectedTodo.text = text
        selectedTodo.save()

        return redirect('/')

def search(request):
    q = request.GET["q"]
    todo = Todo.objects.filter(text__contains=q)
    data = []
    for x in todo:
        data.append(x.text)
    return JsonResponse({
        'data': data
    })

    
