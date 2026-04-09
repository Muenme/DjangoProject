from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'module_project/home.html')