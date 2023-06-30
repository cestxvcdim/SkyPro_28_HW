# Generated by Django 4.2.2 on 2023-06-30 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="название")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="название")),
                ("lat", models.FloatField(verbose_name="широта")),
                ("lng", models.FloatField(verbose_name="долгота")),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20, verbose_name="имя")),
                ("last_name", models.CharField(max_length=20, verbose_name="фамилия")),
                (
                    "username",
                    models.CharField(max_length=20, verbose_name="имя пользователя"),
                ),
                ("password", models.CharField(max_length=20, verbose_name="пароль")),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("user", "Пользователь"),
                            ("admin", "Админ"),
                            ("moderator", "Модератор"),
                        ],
                        default="user",
                        max_length=9,
                        verbose_name="роль",
                    ),
                ),
                ("age", models.PositiveSmallIntegerField(verbose_name="возраст")),
                (
                    "locations",
                    models.ManyToManyField(to="ads.location", verbose_name="локации"),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["username"],
            },
        ),
        migrations.CreateModel(
            name="Ad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="название")),
                ("price", models.PositiveIntegerField(verbose_name="цена")),
                (
                    "description",
                    models.CharField(
                        max_length=500, null=True, verbose_name="описание"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="опубликовано"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ads.user",
                        verbose_name="автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ads.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
    ]