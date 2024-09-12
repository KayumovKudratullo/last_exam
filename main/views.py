from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from . import models

@login_required(login_url='login')
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
        User.objects.create_user(
            password = request.POST['password'],
            username=request.POST['username']
        )
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')  # Redirect to a homepage or dashboard
    return render(request, 'login.html')

@login_required(login_url='login')
def attendance(request):
    attendance = models.StaffAttendance.objects.all()
    return render(request, 'dashboard/attendance/list.html', {"attendances":attendance})

def log_out(request):
    logout(request)
    return redirect('main')