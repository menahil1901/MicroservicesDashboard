# Generated by Django 5.0.2 on 2024-03-19 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_activitylog_customuser_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedependency',
            name='is_admin_dependency',
        ),
    ]
