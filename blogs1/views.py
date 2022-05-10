from django.shortcuts import get_object_or_404, render
from .models import blogs1
# Create your views here.


def allblogs(request):
    b = blogs1.objects
    return render(request, 'blogs1/blogs.html', {'b': b})


def details(request, blog_id):
    blogdetail = get_object_or_404(blogs1, pk=blog_id)
    return render(request, 'blogs1/detail.html', {'blog': blogdetail})
