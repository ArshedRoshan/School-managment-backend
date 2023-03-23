from rest_framework import serializers
from .models import School,Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','email','name','city','pin_code','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 
    
    

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','username','password','school_id','class_id']
        
class Studentsserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username','password']
   

