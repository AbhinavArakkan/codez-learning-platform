from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'public/home.html')

def about(request):
    return render(request, 'public/about.html')

def courses(request):
    return render(request, 'public/courses.html')