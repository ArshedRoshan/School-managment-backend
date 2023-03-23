
from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializers import *
from rest_framework import status
import jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime, timedelta
from admins.models import grade
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@api_view(["POST"])
def school_signup(request):
    if request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"POST"])
def add_student(request,classes):
    try:
        grades = grade.objects.get(classes = classes)
    except ObjectDoesNotExist:
        return Response({'error': f'Class {classes} does not exist'})
    if request.method == 'POST':
        student_data = request.data.get('students')
        print('stuentdata',student_data)
        students = []
        for student_dat in student_data:
            print(type(student_dat))
            # student = Student(
            # class_id = grades )
            print("1",student_dat)
            
            student_dat['class_id'] = grades.classes
            serializer = Studentserializer(data=student_dat,partial=True)
            print('imaerror',serializer.is_valid())
            print('errors',serializer.errors)
            
            if serializer.is_valid():
                students.append(student_dat)
                serializer.save()
            else:
                return Response(serializer.errors)
        if students:
            return Response({'students': students})
        else:
            return Response({'error': 'No valid students provided'})  
        
    return Response({'error': 'This endpoint only accepts POST requests'})
            
    # student = Student(
    #     class_id = grades
    # )
    # serializer = Studentserializer(student,data=request.data)
    # print(serializer)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # return Response(status=status.HTTP_404_NOT_FOUND)
    
#     {
#     "students": [
#         {
#             "name": "john",
#             "username": "John",
#             "school_id": 1,
#             "password": "john"
#         },
#         {
#             "name": "Ram",
#             "username": "ram",
#             "school_id": 1,
#             "password": "ram"
#         }
#     ]
# }


@api_view(['GET','POST'])       
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]  
    
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['name'] = user.name
        token['city'] = user.city
        token['pin_code'] = user.pin_code
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
# class StudentTokenObtainPairView(TokenObtainPairView):
#     serializer_class = StudentTokenObtainPairSerializer

@api_view(['POST'])
def student_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        student = Student.objects.get(username=username)
    except Student.DoesNotExist:
        return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)
    # If the username and password are correct, create a JWT token for the student
    payload = {
        'user_id': student.id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
    }
    token = jwt.encode(payload,settings.SECRET_KEY, algorithm='HS256')

    return Response({'token': token})

@api_view(['GET'])
def display_student_and_filter(request,id,classid=None):
    try:
        if classid:
            student=Student.objects.filter(school_id=id,class_id=classid)
            serializer=Studentserializer(student,many=True)
            return Response(serializer.data)
        student=Student.objects.filter(school_id=id)
        serializer=Studentserializer(student,many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # return( Response('hello'))

@api_view(['PUT'])
def update_details(request,std_id,school_id=None):
    student=Student.objects.get(id=std_id)
    a=request.data.copy()
    if school_id:
        if student.school_id_id !=school_id:
            return Response("This student is not in your school")
    serializer = Studentsserializer(student,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
