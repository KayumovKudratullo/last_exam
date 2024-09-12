from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

from . import models

def main(request):
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    context = {
        'greeting': greeting,
        'today': now.strftime('%Y-%m-%d'),  
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a homepage or dashboard
    return render(request, 'login.html')

def attendance(request):
    attendance = models.StaffAttendance.objects.all()
    return render(request, 'dashboard/attendance/list.html', {"attendances":attendance})