from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=10)
    department=models.CharField(max_length=20)
    rollno=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
