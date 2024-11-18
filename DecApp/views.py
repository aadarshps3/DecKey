from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request,'Login.html')
