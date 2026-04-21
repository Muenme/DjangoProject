from django.shortcuts import render, get_object_or_404
from .models import Weapon_type
from .models import Dop_stat_type
from .models import Element
from .models import Character
from .models import Weapon
from .models import Artifacts
from .models import Build

# Create your views here.
def home(request):
    
    latest_builds = Build.objects.select_related(
        'character', 'weapon', 'artifacts'
    ).all()[:10] 

    count_builds = Build.objects.count()

    builds = Build.objects.all()

    context = {
        'count_builds': count_builds,
        'builds': builds,
        'latest_builds': latest_builds
    }

    return render(request, 'module_project/home.html', context)

def build_detail(request, pk):
    build = get_object_or_404(Build, pk=pk) 
    
    context = {
        'build': build,
    }
    return render(request, 'module_project/build_detail.html', context)