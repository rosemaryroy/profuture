# Generated by Django 4.0.2 on 2022-04-22 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mod', '0005_delete_project_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_table',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('documentation', models.CharField(max_length=400)),
                ('project', models.FileField(upload_to='projects')),
                ('userid', models.IntegerField(default=0)),
                ('pro_req', models.IntegerField(default=0)),
                ('platformid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_mod.platform')),
            ],
        ),
    ]
