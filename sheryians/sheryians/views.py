from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def course_detail(request):
    return render(request, "course_detail.html")