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
    path('dashboard/slider/delete/<int:id>',delete_slider,name='dashboard.slider.delete')
    
]