import uuid

from django.db import models
from django.contrib.auth.models import User  # Import the default User model


class Microservice(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dashboard_microservice'


class ServiceDependency(models.Model):
    source_microservice = models.ForeignKey(Microservice, on_delete=models.CASCADE, related_name='source_dependencies')
    target_microservice = models.ForeignKey(Microservice, on_delete=models.CASCADE, related_name='target_dependencies')
    relationship = models.CharField(max_length=100)
    is_admin_dependency = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.source_microservice.name} -> {self.target_microservice.name}"

    class Meta:
        db_table = 'dashboard_servicedependency'


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
    ]
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'dashboard_activitylog'


    def __str__(self):
        return f'{self.action} by {self.user.username} at {self.timestamp}'

class WelcomeNotification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField()
