# Generated by Django 5.0.2 on 2024-03-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_activitylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedependency',
            name='is_admin_dependency',
            field=models.BooleanField(default=False),
        ),
    ]
