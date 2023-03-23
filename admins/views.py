from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from admins.serializer import *
from user.models import *
from user.serializers import *

# Create your views here.
@api_view(['GET','POST'])
def add_grade(request):
    serializer = gradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET','POST'])
def view_school(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def admin_filter_school_grade(request,id,classid=None):
    if classid:
        student=Student.objects.filter(school_id=id,class_id=classid)
        serializer=Studentserializer(student,many=True)
        return Response(serializer.data)
    student=Student.objects.filter(school_id=id)
    serializer=Studentserializer(student,many=True)
    return Response(serializer.data)



    
