from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # include = ['name', 'age']
        exclude = ['id', 'age']
        # fields = '__all__'