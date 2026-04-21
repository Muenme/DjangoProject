from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Weapon_type
from .models import Dop_stat_type
from .models import Element
from .models import Character
from .models import Weapon
from .models import Artifacts
from .models import Build

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

def build_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        character_id = request.POST.get('character')
        weapon_id = request.POST.get('weapon')
        artifacts_id = request.POST.get('artifacts')

        if name and character_id and weapon_id and artifacts_id:
            build = Build.objects.create(
                name=name,
                character_id=character_id,
                weapon_id=weapon_id,
                artifacts_id=artifacts_id
            )
            messages.success(request, 'Сборка успешно создана!')
            return redirect('build_detail', pk=build.pk)
        else:
            messages.error(request, 'Заполните все поля')

    context = {
        'characters': Character.objects.all(),
        'weapons': Weapon.objects.all(),
        'artifacts': Artifacts.objects.all(),
        'elements': Element.objects.all(),
    }
    return render(request, 'module_project/build_create.html', context)