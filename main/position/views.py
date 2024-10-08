from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from main import models

@login_required(login_url='login')
def list(request):
    position=models.Position.objects.all()
    context = {
        'positions':position
    }
    return render(request,'dashboard/position/list.html', context)

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        models.Position.objects.create(
            name=request.POST['name'],
        )
        return redirect('position_list')
    return render(request, 'dashboard/position/create.html',)

@login_required(login_url='login')
def delete(request, id):
    models.Position.objects.get(id=id).delete()
    return redirect('position_list')

@login_required(login_url='login')
def update(request, id):
    position = get_object_or_404(models.Position, id=id)
    if request.method == 'POST':
        position.name = request.POST['name']
        position.save()
        return redirect('position_list')
    return render(request, 'dashboard/position/update.html')