# Generated by Django 5.0.2 on 2024-03-19 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_customuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
