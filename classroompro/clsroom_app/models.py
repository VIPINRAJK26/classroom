from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class TeacherModel(models.Model):
#     username=models.CharField(max_length=100)
#     email=models.EmailField()
#     teacher_name=models.CharField(max_length=100)
#     subject=models.CharField(max_length=100)
#     password=models.CharField(max_length=30)

#     def __str__(self):
#         return self.username




class TeacherProfile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.username
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Subject(models.Model):
    subject=models.CharField(max_length=100)

    def __str__(self) :
        return self.subject


class Classes(models.Model):
    section=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    videos=models.FileField(upload_to='videos')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.section


