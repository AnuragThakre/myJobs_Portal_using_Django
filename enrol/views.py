from django.shortcuts import render
from .forms import studentRegistration,TeacherRegistration
# Create your views here.
def student_form(request):
    fm=studentRegistration()
    return render(request,'enrol/student.html',{'form':fm})

def teacher_form(request):
    fm=TeacherRegistration()
    return render(request,'enrol/teacher.html',{'form':fm})