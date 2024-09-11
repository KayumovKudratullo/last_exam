from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from main import models


def list(request):
    employe=models.Employee.objects.all()
    context = {
        'employees':employe
    }
    return render(request,'dashboard/staff/list.html', context)

def create(request):
    positions = models.Position.objects.all()
    if request.method == 'POST':
        # Get the value of is_staff, defaulting to 'off' if not checked
        is_active = request.POST.get('is_active', 'off')
        
        # Convert 'on' to True and 'off' to False
        if is_active == 'on':
            status = True
        else: 
            status = False

        # Create a new employee record
        position = models.Position.objects.get(id=request.POST['position'])
        models.Employee.objects.create(
            full_name=request.POST['full_name'],
            is_active=status, 
            position = position
        )
        return redirect('staff_list')
    return render(request, 'dashboard/staff/create.html', {'positions':positions})


def detail(request, id ):
    data = models.Employee.objects.get(id=id)
    context = {
        'employee':data
    }
    return render(request, 'dashboard/staff/detail.html', context)


def delete(request, id):
    models.Employee.objects.get(id=id).delete()
    return redirect('staff_list')


def update(request, id):
    staff = get_object_or_404(models.Employee, id=id)
    position = models.Position.objects.all()
    context = {
        'employee':staff,
        'positions':position
    }
 
    # Get the value of is_staff, defaulting to 'off' if not checked
    is_staff = request.POST.get('is_staff', 'off')

    if is_staff == 'on':
        print(is_staff)
        status = True
    else:  
        print(is_staff)
        status = False

    if request.method == 'POST':
        position = models.Position.objects.get(id=request.POST['position'])
        staff.full_name = request.POST['full_name']
        staff.position = position
        staff.is_active = status
        staff.save()
        return redirect('staff_list')
    return render(request, 'dashboard/staff/update.html', context)