from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html', {})

def achievements_view(request):
    return render(request, 'achievements.html', {})

def neville_view(request):
    return render(request, 'neville_profile.html', {})

def emriz_view(request):
    return render(request, 'emriz_profile.html', {})