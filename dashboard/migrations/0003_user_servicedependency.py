# Generated by Django 5.0.2 on 2024-02-28 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_microservice_deployment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=100)),
                ('source_microservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_dependencies', to='dashboard.microservice')),
                ('target_microservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_dependencies', to='dashboard.microservice')),
            ],
        ),
    ]
