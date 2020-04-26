
from django.shortcuts import render, redirect
from .models import *
from django.template import loader
from .forms import *


def home(request):
    notes = Note.objects.all()
    form = Noteform()
    context = {'notes': notes, 'form': form}
    if request.method == 'POST':
        form = Noteform(request.POST)
        if form.is_valid():
            form.save()
        # else:
        #     return redirect('update/')
        return redirect('/')

    return render(request,'home.html', context)
def update(request, id):
    Notes = Note.objects.get(id=id)
    form = Noteform(instance=Notes)
    context = {'item':Notes, 'form': form}
    if request.method == 'POST':
        form = Noteform(request.POST, instance=Notes)
        if form.is_valid():
            form.save()
    #     # context ={'Message':'Upload Suckessfully'}
        return redirect('/')

    return render(request, 'update.html', context)

def delete(request, id):
    item = Note.objects.get(id=id)
    context = {'item':item}

    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html', context)
