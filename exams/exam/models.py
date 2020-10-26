from django.db import models

# Create your models here.
class Exam(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    time_limit=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Questions(models.Model):
    SOLUTION_CHOICES=[
        ("SS","SELECT SOLUTION"),
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
    ]
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    solution=models.CharField(max_length=2,choices=SOLUTION_CHOICES,default="SS")

    def __str__(self):
        return self.name
