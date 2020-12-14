from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import get_user_model
from accounts.views import User
from django.contrib.auth.models import User
from todo_list.models import todo_list
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def todo(request):
    Task_obj = todo_list.objects.all().order_by('-date')
    return render(request, 'todo.html',{"Task_obj": Task_obj})

@login_required(login_url='/')
def show_todo(request):
    items = todo_list.objects.all()
    return render(request, 'list.html', {"items": items})

@login_required
@csrf_exempt    
def task_list(request):
    if request.method == 'POST':
        author=request.user
        date = timezone.now()
        task = request.POST['add_task']
        
        Task = todo_list.objects.create(date=date, task=task, author=request.user)
        Task_obj = todo_list.objects.all().order_by('-date')
        return HttpResponseRedirect("/todo_list")
        #return render(request,'todo1.html',{"Task_obj": Task_obj})
    else:
        return render(request,'todo1.html')

@csrf_exempt 
def delete_todo(request, task_id):
    print(task_id)
    d = todo_list.objects.get(id=task_id)
    d.delete()
    return HttpResponseRedirect("/todo_list")

# @csrf_exempt
# def edit_todo(request, task_id):
#     todo_list.objects.filter(id=task_id).update(task=task_list)
    
#     return HttpResponseRedirect("/todo_list")
    