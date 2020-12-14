from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import Comment_section
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    comment_obj = Comment_section.objects.all().order_by('-date')
    c = Comment_section.objects.all().count()
    return render(request, 'index.html',{'comment_obj':comment_obj,'count':c})


def all_comment(request):
    comment_obj = Comment_section.objects.all().order_by('-date')
    return render(request, 'comment.html',{'comment_obj':comment_obj})


@csrf_exempt
def Comment(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        comment = request.POST['comment']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin_code']
        date = timezone.now()

        comment_obj = Comment_section.objects.create(first_name=first_name,last_name=last_name,email=email,comment=comment,city=city,state=state,pin_code=pin_code,date=date)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")