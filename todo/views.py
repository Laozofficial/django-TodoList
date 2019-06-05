from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

from .models import Todo
# from django.db.models import FloatField
# from django.db.models.function import Cast


# Create your views here.
def index(request):
    todo = Todo.objects.all()[:100]

    context = {
        'todo' : todo
    }
    # return HttpResponse('hello world from todo app')
    return render(request, 'todo/index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }

    return render(request, 'todo/views.html', context)

def delete(request, id):
    todo = Todo.objects.get(id=id).delete()

    # context = {
    #     'todo': todo
    # }

    return redirect('/')

def add(request):
    # todo Todo.objects.create()
    return render(request, 'todo/add.html')

def add_todo(request):
    if request.method == 'POST':
        
        title = request.POST.get('todo_title', None)
        description = request.POST.get('todo_description', None)
        your_name = request.POST.get('your_name', None)

        # if title is None:
        #     return HttpResponse('')


        name = Todo.objects.create(title=title, desciption=description, posted_by=your_name)
        name.save()
        return redirect('/')

def edit_todo(request, id):

     todo = Todo.objects.get(id=id)

     context = {
        'todo': todo
     }

     return render(request, 'todo/edit.html', context)
    
def update(request, id):
    
    # todo = Todo.objects.get(id=id)

    if request.method == 'POST':

        title = request.POST.get('todo_title', None)
        description = request.POST.get('todo_description', None)
        your_name = request.POST.get('your_name', None)

        name = Todo.objects.filter(id=id).update(title=title, desciption=description, posted_by=your_name)
        # name.update()
        return redirect('/')

