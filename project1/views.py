from django.shortcuts import render
from app.models import Student

def abc(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
