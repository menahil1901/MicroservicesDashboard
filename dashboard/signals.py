from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import ActivityLog

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # Check if the login was through your custom login URL
    if request.resolver_match.url_name == 'account_login':
        ActivityLog.objects.create(user=user, action='LOGIN')

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    # Check if the logout was through your custom logout URL
    if request.resolver_match.url_name == 'account_logout':
        ActivityLog.objects.create(user=user, action='LOGOUT')
