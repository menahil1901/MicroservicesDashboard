from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import override_settings

class StaffAccessSecurityTest(TestCase):
    @override_settings(MIDDLEWARE=[
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',  # Add this line
    ])
    def setUp(self):
        # Create a regular user
        self.user = User.objects.create_user(username='regular_user', password='testpassword')
        # Create a staff user
        self.staff_user = User.objects.create_user(username='staff_user', password='testpassword', is_staff=True)
        # URL for a view restricted to staff members
        self.staff_only_url = reverse('service_dependency_list')  # Change this to the actual URL name of your staff-only view
        # Create a RequestFactory instance
        self.factory = RequestFactory()

    def test_regular_user_access(self):
        # Create a request object with a regular user
        request = self.factory.get(self.staff_only_url)
        request.user = self.user
        # Attempt to access the staff-only view
        response = self.client.get(self.staff_only_url, request=request)
        # Ensure regular users are denied access
        self.assertEqual(response.status_code, 403)  # Expecting Forbidden status code

    def test_staff_user_access(self):
        # Log in as a staff user
        self.client.login(username='staff_user', password='testpassword')
        # Attempt to access the staff-only view
        response = self.client.get(self.staff_only_url)
        # Ensure staff users have access
        self.assertEqual(response.status_code, 200)  # Expecting OK status code
