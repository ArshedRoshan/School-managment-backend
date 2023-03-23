from django.contrib import admin
from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('school_signup',school_signup,name='school_signup'),
    path('add_student/<int:classes>',add_student,name='add_student'),
    path('display_student_and_filter/<int:id>',display_student_and_filter,name='display_student_and_filter'),
    path('display_student_and_filter/<int:id>/<int:classid>',display_student_and_filter,name='display_student_and_filter'),
    path('update_details/<int:std_id>',update_details,name='update_details'),
    path('update_details/<int:std_id>/<int:school_id>',update_details,name='update_details'),
    path('',getRoutes,name='routes'),
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
     path('student/login/', student_login, name='student_login'),
    # path('student/login/', StudentTokenObtainPairView.as_view(), name='student-login'),
]