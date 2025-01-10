from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request,"todo_list.html",{"todos": todos})
    
def todo_delete(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return HttpResponseRedirect("/")
    
