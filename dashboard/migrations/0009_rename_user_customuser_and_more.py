# Generated by Django 5.0.2 on 2024-03-18 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_servicedependency_is_admin_dependency'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
        migrations.RenameField(
            model_name='activitylog',
            old_name='user',
            new_name='CustomUser',
        ),
    ]
