from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from main import models


def list(request):
    shifts=models.Shift.objects.all()
    context = {
        'shifts':shifts
    }
    return render(request,'dashboard/shift/list.html', context)

def create(request):
    if request.method == 'POST':
        models.Shift.objects.create(
            shift_type=request.POST['shift_type'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time']
        )
        return redirect('shift_list')
    return render(request, 'dashboard/shift/create.html')

def delete(request, id):
    models.Shift.objects.get(id=id).delete()
    return redirect('shift_list')

def update(request, id):
    shift = models.Shift.objects.get(id=id)
    if request.method == 'POST':
        shift.shift_type = request.POST['shift_type']
        shift.start_time = request.POST['start_time']
        shift.end_time = request.POST['end_time']
        shift.save()
        return redirect('shift_list')
    return render(request, 'dashboard/shift/update.html', {'shift':shift})