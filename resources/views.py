from django.shortcuts import render

# Create your views here.
def ResourcesPageViews(request):
    return render(request,'resources/resources.html')