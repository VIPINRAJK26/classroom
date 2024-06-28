from django import forms
# from clsroom_app.models import TeacherModel 
from django.contrib.auth.models import User
from clsroom_app.models import Classes
from .models import TeacherProfile, StudentProfile


class TeacherRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password']
        widgets={
            'first_name':forms.TextInput,
            'username':forms.TextInput,
            'email':forms.EmailInput,
            'password':forms.PasswordInput
        }

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password']
        widgets={
            'first_name':forms.TextInput,
            'username':forms.TextInput,
            'email':forms.EmailInput,
            'password':forms.PasswordInput
        }

class TeacherLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput,
            'password':forms.PasswordInput
        }

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput,
            'password':forms.PasswordInput
        }

class EditDetailsForm(forms.ModelForm):
    class Meta:
        model=Classes
        fields=['section','description','subject']
        widgets={
            'section':forms.TextInput,
            'description':forms.TextInput,
            'subject':forms.TextInput
        }