from django.shortcuts import render

from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request,"todo_list.html",{"todos": todos})
    return render(request,"todo_list.html",{"todos": todos})

    
