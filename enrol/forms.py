from django import forms
from .models import User

class studentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['student_name','email','password']

class TeacherRegistration(studentRegistration):
    class Meta(studentRegistration.Meta):
        fields=['teacher_name','email','password']