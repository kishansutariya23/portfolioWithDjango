from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def projects(request):
    return render(request,'core/projects.html')