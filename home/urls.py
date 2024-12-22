from django.urls import path, include
from .views import home, hello_world, student_details

urlpatterns = [
    path('', home),
    path('hw', hello_world),
    path('sd', student_details),
]