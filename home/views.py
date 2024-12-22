from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view()
def home(request):
    return Response({'Status' : 200, 'msg' : 'Welcome to our Home page...'})

@api_view(['POST'])
def hello_world(request):
    return Response({'Status' : 200, 'msg' : 'Say hello to the beautiful world...'})

@api_view(['GET'])
def student_details(request):
    student_data = Student.objects.all()
    ser_student = StudentSerializer(student_data, many = True)
    return Response({'Status' : 200, 'payload' : ser_student.data})
