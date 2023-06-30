from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    lat = models.FloatField(verbose_name="широта")
    lng = models.FloatField(verbose_name="долгота")

    class Meta:

        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ("user", "Пользователь"),
        ("admin", "Админ"),
        ("moderator", "Модератор")
    ]

    first_name = models.CharField(max_length=20, verbose_name="имя")
    last_name = models.CharField(max_length=20, verbose_name="фамилия")
    username = models.CharField(max_length=20, verbose_name="имя пользователя")
    password = models.CharField(max_length=20, verbose_name="пароль")
    role = models.CharField(max_length=9, choices=ROLES, default="user", verbose_name="роль")
    age = models.PositiveSmallIntegerField(verbose_name="возраст")
    locations = models.ManyToManyField(Location, verbose_name="локации")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="название")

    class Meta:

        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    price = models.PositiveIntegerField(verbose_name="цена")
    description = models.CharField(max_length=500, null=True, verbose_name="описание")
    is_published = models.BooleanField(default=False, verbose_name="опубликовано")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="изображение")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="категория")

    class Meta:

        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
