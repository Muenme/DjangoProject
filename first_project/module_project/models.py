from django.db import models
#БД
class Weapon_type(models.Model):
    """
    Модель для хранения типов оружия.
    """
    weapon_type_name = models.CharField(
        max_lenght = 50,
        verbose_name = "Тип оружия")#Название строчки
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.weapon_type_name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Тип оружия"  # Название в единственном числе
        verbose_name_plural = "Типы оружия"  # Название во множественном числе            

class Dop_stat_type(models.Model):
    """
    Модель для типов доп. статов
    """
    dop_stat_name = models.CharField(
        max_lenght = 50,
        verbose_name = "Дополнительная характеристика")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.dop_stat_name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Тип доп. стата"  # Название в единственном числе
        verbose_name_plural = "Типы доп. статов"  # Название во множественном числе 

class Element(models.Model):
    """
    Модель для хранения элементов.
    """
    element_name = models.CharField(
        max_lenght = 50,
        verbose_name = "Элемент")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.element_name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Элемент"  # Название в единственном числе
        verbose_name_plural = "Элементы"  # Название во множественном числе 

class Сharacter(models.Model):
    """
    Модель для хранения персонажа.
    """
    # Изображение
    сharacter_image = models.ImageField(
        upload_to='character_image/',  # Папка для загрузки файлов
        verbose_name="Изображение персонажа", 
        blank=True, 
        null = True
    )    
    name = models.CharField(
        max_lenght = 100,
        verbose_name = "Имя персонажа")
    type_weapon = models.ForeignKey(
        Weapon_type, 
        on_delete = models.CASCADE,
        verbose_name = "Тип оружия")
    element = models.ForeignKey(
        Element, 
        on_delete = models.CASCADE,
        verbose_name = "Элемент")
    health = models.IntegerField(
        verbose_name = "Здоровье")
    attack_power = models.IntegerField(
        verbose_name = "Сила атаки")
    protection = models.IntegerField(
        verbose_name = "Защита")
    mastery_elements = models.IntegerField(
        verbose_name = "Мастерство стихий")
    description = models.CharField(
        max_lenght = 1000,
        blank = True,
        verbose_name = "Описание персонажа")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Персонаж"  # Название в единственном числе
        verbose_name_plural = "Персонажи"  # Название во множественном числе 

class Weapon(models.Model):
    """
    Модель для хранения конкретного оружия.
    """   
    weapon_image = models.ImageField(
        upload_to='weapon_image/',  # Папка для загрузки файлов
        verbose_name="Изображение оружия", 
        blank=True, 
        null = True)
    name = models.CharField(
        max_lenght = 100,
        verbose_name = "Название оружия")
    type_weapon = models.ForeignKey(
        Weapon_type, 
        on_delete = models.CASCADE,
        verbose_name = "Тип оружия")    
    dop_stat_name = models.ForeignKey(
        Dop_stat_type, 
        on_delete = models.CASCADE,
        verbose_name = "Дополнительная характеристика")
    dop_stat = models.IntegerField(
        verbose_name = "Значение дополнительной характеристики"
    )
    description = models.CharField(
        max_lenght = 1000,
        blank = True,
        verbose_name = "Описание оружия")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Оружие"  # Название в единственном числе
        verbose_name_plural = "Оружии"  # Название во множественном числе 

class Artifacts(models.Model):
    """
    Модель для хранения конкретного оружия.
    """   
    artifacts_image = models.ImageField(
        upload_to='artifacts_image/',  # Папка для загрузки файлов
        verbose_name="Изображение сета артефактов", 
        blank=True, 
        null = True)
    name = models.CharField(
        max_lenght = 100,
        verbose_name = "Название сета артефактов")
    dop_stat_name = models.ForeignKey(
        Dop_stat_type, 
        on_delete = models.CASCADE,
        verbose_name = "Дополнительная характеристика")
    dop_stat = models.IntegerField(
        verbose_name = "Значение дополнительной характеристики"
    )
    description = models.CharField(
        max_lenght = 1000,
        blank = True,
        verbose_name = "Описание сета артефактов")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Сет артефакта"  # Название в единственном числе
        verbose_name_plural = "Сеты артефактов"  # Название во множественном числе \

class Build(models.Model):
    name = models.CharField(
        max_lenght = 100,
        verbose_name = "Название сборки")
    character = models.ForeignKey(
        Сharacter,
        on_delete = models.CASCADE,
        verbose_name = "Персонаж")
    weapon = models.ForeignKey(
        Weapon,
        on_delete = models.CASCADE,
        verbose_name = "Оружие")
    artifacts = models.ForeignKey(
        Artifacts,
        on_delete = models.CASCADE,
        verbose_name = "Артефакты")
    def __str__(self):
        """
        Строковое представление объекта.
        Используется в админке и при выводе в шаблонах.
        """
        return self.name
    class Meta:
        # Метаданные модели для админки и сортировки
        verbose_name = "Сборка"  # Название в единственном числе
        verbose_name_plural = "Сборки"  # Название во множественном числе 