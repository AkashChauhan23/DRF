from django.urls import path, include
from .views import home, hello_world, student_details, post_student_details, put_student_details

urlpatterns = [
    path('', home),
    path('hello-world', hello_world),
    path('student-details-get', student_details),
    path('student-details-post', post_student_details),
    path('student-details-put/<id>/', put_student_details),
]
