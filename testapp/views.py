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


def about_index(request):
    about_data=AboutSection.objects.all()
    return render(request,'pages/about_section/index.html',{'about':about_data})

def add_about(request):
    return render(request,'pages/about_section/create_about.html')

def save_about(request):
    if request.method == "POST":
        title = request.POST.get("title")
        sub_title = request.POST.get("sub_title")
        sub_heading = request.POST.get("sub_heading")
        description = request.POST.get("description")

        image1 = request.FILES.get("image1")
        image2 = request.FILES.get("image2")

        raw_list = request.POST.get("my_list")

        # Convert textarea lines → Python list
        my_list = [
            item.strip()
            for item in raw_list.splitlines()
            if item.strip()
        ]

        AboutSection.objects.create(
            title=title,
            sub_title=sub_title,
            sub_heading=sub_heading,
            description=description,
            image1=image1,
            image2=image2,
            my_list=my_list
        )
        messages.success(request,'successfullt added about data!!')
        return redirect("dashboard.about.index.html")


def edit_about(request,id):
    about_edit=AboutSection.objects.filter(id=id).first()
    return render(request,'pages/about_section/edit_about.html',{'about_edit':about_edit})


def update_about(request,id):
    if request.method == "POST":
        title = request.POST.get("title")
        sub_title = request.POST.get("sub_title")
        sub_heading = request.POST.get("sub_heading")
        description = request.POST.get("description")

        image1 = request.FILES.get("image1")
        image2 = request.FILES.get("image2")

        raw_list = request.POST.get("my_list")

        # Convert textarea lines → Python list
        my_list = [
            item.strip()
            for item in raw_list.splitlines()
            if item.strip()
        ]

        update_about=AboutSection.objects.get(id=id)
        update_about.title=title
        update_about.sub_title=sub_title
        update_about.description=description
        update_about.sub_heading=sub_heading
        update_about.my_list=my_list
        if image1:
            update_about.image1=image1
        if image2:
            update_about.image2=image2
        update_about.save()

        messages.success(request,'successfully update about data!!')
        return redirect('dashboard.about.index.html')
    
def delete_about(request,id):
    about=AboutSection.objects.filter(id=id)
    about.delete()
    messages.success(request,'successfully deleted about data!!')
    return redirect('dashboard.about.index.html')

def services_index(request):
    service_data=Services.objects.all()
    return render(request,'pages/services/index.html',{'service_data':service_data})

def add_service(request):
    return render(request,'pages/services/create_service.html')

def save_service(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        icon=request.FILES.get('icon')

        Services.objects.create(
            title=title,
            description=description,
            icon=icon,
        )
        messages.success(request,'Successfully added service data!!')
    return redirect('dashboard.services.index.html')

def edit_service(request,id):
    service_edit=Services.objects.filter(id=id).first()
    return render(request,'pages/services/edit_service.html',{'service_data':service_edit})


def update_service(request,id):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        icon=request.FILES.get('icon')

        update_service=Services.objects.get(id=id)
        update_service.title=title
        update_service.description=description
        if icon:
            update_service.icon=icon
        update_service.save()

    
        messages.success(request,'Successfully update service data!!')

    return redirect('dashboard.services.index.html')

def delete_service(request,id):
    service=Services.objects.filter(id=id)
    service.delete()
    messages.success(request,'Successfully delete service data!!')
    return redirect('dashboard.services.index.html')






