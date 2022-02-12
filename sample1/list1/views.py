from django.shortcuts import render
from django.http import HttpResponse
from.models import list1

def index(request):
    list_image = list1.objects.all()
    imgs= list1.objects.get(id=1)
    # return HttpResponse("<h1>Welcome to django</h1>")
    return render(request, 'index.html',{'ls':list_image,'imgs':imgs})

# Create your views here.
