# Generated by Django 4.0.2 on 2022-04-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mod', '0003_project_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_table',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]
