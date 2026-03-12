from django.db import models

class Weapon_type(models.Model):
    """
    Модель для хранения типов оружия.
    """
    weapon_type_id = IntegerField()
    weapon_type_name = models.CharField(max_lenght = 50)
    verbose_name = "Тип оружия"

class Element():
    """
    Модель для хранения элементов.
    """
    element_id = models.IntegerField()
    element_name = models.CharField(max_lenght = 50)
    verbose_name = "Элемент"

class Сharacter(models.Model):
    """
    Модель для хранения типов оружия.
    """
    name = models.CharField(max_lenght = 100)
    type_weapon = models.ForeignKey(Weapon_type, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    health = models.IntegerField()
    attack_power = models.IntegerField()
    protection = models.IntegerField()
    mastery_elements = models.IntegerField()
    verbose_name = "Персонаж"

class Weapon():
    name = models.CharField(max_lenght = 100)
    dop_stat_name = models.CharField(max_lenght = 100)
    dop_stat = models.IntegerField()
    dop = models.CharField(max_lenght = 1000)