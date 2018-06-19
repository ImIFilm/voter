from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from lecturers.models import Lecturer
# Create your views here.
def home(request):
    courses = Course.objects
    return render(request, 'courses/home.html',{'courses':courses})


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html',{'course':course})

def who(request):
    courses = Course.objects
    lecturers=Lecturer.objects
    return render(request, 'courses/who.html',{'courses':courses, 'lecturers':lecturers})