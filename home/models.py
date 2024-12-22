from django.db import models
GENDER_CHOICE = (('MALE', 'MALE'),('FEMALE', 'FEMALE'))

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='MALE')

    def __str__(self):
        return f'{self.name} {self.age}'
