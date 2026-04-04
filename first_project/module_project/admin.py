from django.contrib import admin
from .models import Weapon_type, Dop_stat_type, Element, Character, Weapon, Artifacts, Build

# Register your models here.
@admin.register(Weapon_type)
class Weapon_typeAdmin(admin.ModelAdmin):
    """
    Настройки административного интерфейса для модели Weapon_type.
    Определяет, как типы оружий будут отображаться и управляться в админке.
    """
    
    # Поля, отображаемые в списке всех авторов
    list_display = ['weapon_type_name']
    
    # Поля, по которым можно выполнять поиск
    search_fields = ['weapon_type_name']

@admin.register(Dop_stat_type)    
class Dop_stat_typeAdmin(admin.ModelAdmin):

    list_display = ['dop_stat_name']

    search_fields = ['dop_stat_name']

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):

    list_display = ['element_name']

    search_fields = ['element_name']

@admin.register(Сharacter)
class CharacterAdmin(admin.ModelAdmin):

    list_display = ['сharacter_image', 'name', 'type_weapon', 'element', 'health', 'attack_power', 'protection', 'mastery_elements', 'description']

    search_fields = ['name', 'type_weapon', 'element', 'health', 'attack_power', 'protection', 'mastery_elements', 'description']

    list_filter = ['type_weapon', 'element']

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):

    list_display = ['weapon_image', 'name', 'type_weapon', 'dop_stat_name', 'dop_stat', 'description']

    search_fields = ['name', 'type_weapon', 'dop_stat_name', 'dop_stat', 'description']

    list_filter = ['type_weapon', 'dop_stat_name']

@admin.register(Artifacts)
class ArtifactsAdmin(admin.ModelAdmin):

    list_display = ['artifacts_image', 'name', 'dop_stat_name', 'dop_stat', 'description']

    search_fields = ['name', 'dop_stat_name', 'dop_stat', 'description']

    list_filter = ['dop_stat_name']

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):

    list_display = ['name', 'character', 'weapon', 'artifacts']

    search_fields = ['name', 'character', 'weapon', 'artifacts']

    list_filter = ['character', 'weapon', 'artifacts']