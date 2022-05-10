from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import jobs
# Create your views here.


def home(request):
    j = jobs.objects
    return render(request, 'jobs/home.html', {'jobs': j})
