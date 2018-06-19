from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lecturer
from django.utils import timezone
# Create your views here.
def home(request):
    lecturers = Lecturer.objects
    return render(request, 'lecturers/home.html',{'lecturers':lecturers})

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            lecturer=Lecturer()
            lecturer.name=request.POST['name']
            lecturer.body=request.POST['body']
            lecturer.url=request.POST['url']
            lecturer.icon=request.FILES['icon']
            lecturer.image=request.FILES['image']
            lecturer.pub_date=timezone.datetime.now()
            lecturer.voter=request.user
            lecturer.save()
            return redirect('/lecturers/' + str(lecturer.id))
        else:
            return render(request, 'lecturers/create.html')
    else:
        return render(request, 'lecturers/create.html')

def detail(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, pk=lecturer_id)
    return render(request, 'lecturers/detail.html',{'lecturer':lecturer})

@login_required
def upvote(request, lecturer_id):
    if request.method=='POST':
        lecturer = get_object_or_404(Lecturer, pk=lecturer_id)
        lecturer.votes_total += 1
        lecturer.save()
        return redirect('/lecturers/' + str(lecturer.id))