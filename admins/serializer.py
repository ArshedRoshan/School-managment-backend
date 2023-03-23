from rest_framework import serializers
from admins.models import *

class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = ['classes']