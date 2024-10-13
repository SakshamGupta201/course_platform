# Generated by Django 5.1.2 on 2024-10-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="courses/"),
                ),
                (
                    "access",
                    models.CharField(
                        choices=[("AN", "Anyone"), ("ER", "Email Required")],
                        default="AN",
                        max_length=120,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PU", "Published"),
                            ("DR", "Draft"),
                            ("CS", "Comming Soon"),
                        ],
                        default="DR",
                        max_length=120,
                    ),
                ),
            ],
        ),
    ]
