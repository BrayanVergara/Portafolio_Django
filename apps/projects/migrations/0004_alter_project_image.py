# Generated by Django 4.2.1 on 2023-11-12 20:58

import apps.projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.project_image_path),
        ),
    ]
