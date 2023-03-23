from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add_grade',add_grade,name='add_grade'),
    path('view_school',view_school,name='view_school'),
    path('admin_filter_school_grade/<int:id>',admin_filter_school_grade,name='admin_filter_school_grade'),
    path('admin_filter_school_grade/<int:id>/<int:classid>',admin_filter_school_grade,name='admin_filter_school_grade'),
    
]