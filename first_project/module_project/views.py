from django.shortcuts import render

# Create your views here.
def home(request):
    
    count_builds = Build.objects.count()

    builds = Build.objects.all()

    context = {
        'count_builds': count_builds,
        'builds': builds
    }

    return render(request, 'module_project/home.html', context)