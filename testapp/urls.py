from django.urls import path
from .views import *

urlpatterns=[
    path('',indexpage,name='index.html'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/sliders/index/',sliders_index,name='dashboard.sliders.index.html'),

    path('dashboard/slider/create/',add_slider,name='dashboard.slider.create'),
    path('dashboard/slider/save/',save_slider,name='dashboard.slider.save'),
    path('dadhboard/slider/edit/<int:id>',edit_slider,name='dashboard.slider.edit'),
    path('dashboard/slider/update/<int:id>',update_slider,name='dashboard.slider.update'),
    path('dashboard/slider/delete/<int:id>',delete_slider,name='dashboard.slider.delete'),


    path('dashboard/about/index/',about_index,name='dashboard.about.index.html'),
    path('dashboard/about/create/',add_about,name='dashboard.about.create'),
    path('dashboard/about/save/',save_about,name='dashboard.about.save'),
    path('dashboard/about/edit/<int:id>/',edit_about,name='dashboard.about.edit'),
    path('dashboard/about/update/<int:id>/',update_about,name='dashboard.about.update'),
    path('dashboard/about/delete/<int:id>',delete_about,name='dashboard.about.delete'),

    path('dashboard/services/index/',services_index,name='dashboard.services.index.html'),
    path('dassboard/services/create/',add_service,name='dashboard.service.add'),
    path('dashboard/services/save/',save_service,name='dashboard.service.save'),
    path('dashboard/services/edit/<int:id>/',edit_service,name='dashboard.service.edit'),
    path('dashboard/services/update/<int:id>/',update_service,name='dashboard.service.update'),
    path('dashboard/service/delete/<int:id>/',delete_service,name='dashboard.service.delete'),
    
]