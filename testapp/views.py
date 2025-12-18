from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'pages/dashboard.html')

def sliders_index(request):
    slider_data=Sliders.objects.all()
    return render(request,'pages/sliders/index.html',{'slider_data':slider_data})

def add_slider(request):
    return render(request,'pages/sliders/create_slider.html')

def save_slider(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        content = request.POST.get('description')
        image = request.FILES.get('image') 

        slider_save=Sliders(
            title=title,
            sub_title=sub_title,
            description=content,
            image=image
        )
        slider_save.save()

        messages.success(request, 'Successfully added slider data!')

    return redirect('dashboard.sliders.index.html')


def edit_slider(request,id):
    edit_slider=Sliders.objects.filter(id=id).first()
    return render(request,'pages/sliders/update_slider.html',{'edit_slider':edit_slider})

def update_slider(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        content = request.POST.get('description')
        image = request.FILES.get('image') 

        slider_update=Sliders.objects.get(id=id)
        slider_update.title=title
        slider_update.sub_title=sub_title
        slider_update.description=content
        if image:
            slider_update.image=image
        slider_update.save()

        messages.success(request,'successfully update slider data!!')
    return redirect('dashboard.sliders.index.html')

def delete_slider(request, id):
    delete_slider=Sliders.objects.filter(id=id)
    delete_slider.delete()
    messages.success(request,'successfully deleted slider data!')
    return redirect('dashboard.sliders.index.html')






