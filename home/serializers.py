from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # include = ['name', 'age']
        # exclude = ['id', 'age']
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'Error' : 'Age is less than 18'})
        return data
