from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
import traceback as tb

@api_view(['GET'])
def home(request):
    return Response({'Status' : 200, 'msg' : 'Welcome to our Home page...'})

@api_view(['GET'])
def hello_world(request):
    return Response({'Status' : 200, 'msg' : 'Say hello to the beautiful world...'})

@api_view(['GET'])
def student_details(request):
    student_data = Student.objects.all()
    serializer = StudentSerializer(student_data, many = True)
    return Response({'Status' : 200, 'payload' : serializer.data})

@api_view(['POST'])
def post_student_details(request):
    print(request.data)
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({'Status' : 403, 'msg' : 'Data shared is not vaild', 'error' : serializer.errors})
    serializer.save()
    return Response({'Status' : 200, 'msg' : 'Data loaded successfully', 'data': request.data})

@api_view(['PUT'])
def put_student_details(request, id):
    try:
        obj_student = Student.objects.get(id=id)
        serializer = StudentSerializer(obj_student, data=request.data)
        if not serializer.is_valid():
            return Response({'Status' : 403, 'error' : serializer.errors})
        serializer.save()
        return Response({'Status' : 200, 'msg' : 'Put query executed successfully...'})
    except Exception as e:
        print("Exception occured---> ", e)
        return Response({'Respnse' : '403', 'msg' : 'Something went wrong...', 'error' : tb.format_exc()})

@api_view(['PATCH'])
def patch_student_details(request):
    try:
        pass
    except Exception as e:
        print("Exception occured---> ", e)
        return Response({'Status' : '403', 'msg' : 'Something went wrong...', 'error' : tb.format_exc()})