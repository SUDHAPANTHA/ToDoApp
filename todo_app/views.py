from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request,"todo_list.html",{"todos": todos})
    
def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect("/")
def todo_create(request):
    if request.method == "GET":
        return render(request,"todo_create.html")
    else:
        title = request.POST["title"]
        todo = Todo(title=title)
        todo.save
        return HttpResponseRedirect("/")
def todo_update(request, id):
            todo = Todo.objects.get(id=id)
            if request.method == "GET":
                return render(request, "todo_update.html", {"todo": todo},)
            else:
                todo.title = request.POST["title"]
                todo.save()
                return HttpResponseRedirect("/")
    
