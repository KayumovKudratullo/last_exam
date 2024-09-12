from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from main import models

@login_required(login_url='login')
def list(request):
    employe=models.StaffShift.objects.all()
    context = {
        'employees':employe
    }
    return render(request,'dashboard/shiftstaff/list.html', context)

@login_required(login_url='login')
def create(request):
    staff = models.Employee.objects.all()
    shift = models.Shift.objects.all()
    context = {
        "staffs":staff,
        "shifts":shift
    }
    if request.method=='POST':
        employee = models.Employee.objects.get(id=request.POST['staff'])
        shift = models.Shift.objects.get(id=request.POST['shift'])
        models.StaffShift.objects.create(
            employee=employee,
            shift=shift
            ) 
        return redirect('staffShift_list')
    return render(request, 'dashboard/shiftstaff/create.html', context)

@login_required(login_url='login')
def detail(request, id ):
    data = models.Employee.objects.get(id=id)
    context = {
        'employee':data
    }
    return render(request, 'dashboard/staff/detail.html', context)

@login_required(login_url='login')
def delete(request, id):
    models.Employee.objects.get(id=id).delete()
    return redirect('staff_list')

@login_required(login_url='login')
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