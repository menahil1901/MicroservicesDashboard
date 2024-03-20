from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .models import Microservice, ServiceDependency, ActivityLog
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db import models
from .forms import ServiceDependencyForm, CustomUserCreationForm, UserForm
from django.contrib.auth import login
from django.contrib import messages




class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class MicroserviceListView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        microservices = Microservice.objects.all()

        context = {
            'microservices': microservices,
            'statuses': ['Healthy', 'Warning', 'Critical'],
        }

        return render(request, self.template_name, context)


class MicroserviceCreateView(CreateView):
    model = Microservice
    template_name = 'microservice_form.html'
    fields = '__all__'
    success_url = reverse_lazy('dashboard')


class MicroserviceUpdateView(UpdateView):
    model = Microservice
    template_name = 'microservice_form.html'
    fields = '__all__'
    success_url = reverse_lazy('dashboard')


class MicroserviceDeleteView(DeleteView):
    model = Microservice
    template_name = 'microservice_confirm_delete.html'
    success_url = reverse_lazy('dashboard')


class ServiceDependencyListView(View):
    template_name = 'service_dependency_list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        dependencies = ServiceDependency.objects.all()
        return render(request, self.template_name, {'dependencies': dependencies})


class ServiceDependencyCreateView(View):
    template_name = 'service_dependency_form.html'
    form_class = ServiceDependencyForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service dependency created successfully.')
            return redirect('service_dependency_list')
        else:
            messages.error(request, 'Failed to create service dependency. Please check the form.')
            messages.add_message(request, messages.ERROR, 'Please check the form for errors.') # Add this line for clarity
        return render(request, self.template_name, {'form': form, 'error': True})

class ServiceDependencyUpdateView(View):
    template_name = 'service_dependency_form.html'
    form_class = ServiceDependencyForm

    def get(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        dependency = get_object_or_404(ServiceDependency, pk=pk)
        form = self.form_class(instance=dependency)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        dependency = get_object_or_404(ServiceDependency, pk=pk)
        form = self.form_class(request.POST, instance=dependency)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service dependency updated successfully.')
            return redirect('service_dependency_list')
        else:
            messages.error(request, 'Failed to update service dependency. Please check the form.')
            messages.add_message(request, messages.ERROR, 'Please check the form for errors.') # Add this line for clarity
        return render(request, self.template_name, {'form': form, 'error': True})

class ServiceDependencyDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        dependency = get_object_or_404(ServiceDependency, pk=pk)
        dependency.delete()
        messages.success(request, "Dependency deleted successfully.")
        return redirect('service_dependency_list')

    def get(self, request, *args, **kwargs):
        messages.info(request, "Deletion canceled.")
        return redirect('service_dependency_list')
class CreateUserView(View):
    template_name = 'create_user.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('user_list')
        return render(request, self.template_name, {'form': form})

class UpdateUserView(View):
    template_name = 'update_user.html'

    def get(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        return render(request, self.template_name, {'form': form, 'user': user})

    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_list')
        return render(request, self.template_name, {'form': form, 'user': user})

class DeleteUserView(View):
    template_name = 'delete_user.html'

    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        user = get_object_or_404(User, pk=pk)
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_list')

class UserListView(View):
    template_name = 'user_list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        users = User.objects.all()
        context = {'users': users, 'success_message': messages.get_messages(request)}
        return render(request, self.template_name, context)

class ActivityLogListView(ListView):
    model = ActivityLog
    template_name = 'activity_log_list.html'
    context_object_name = 'activity_logs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_logs = ActivityLog.objects.all()  # Query all activity logs
        print("Activity Logs:", activity_logs)  # Print activity logs for debugging
        context['activity_logs'] = activity_logs
        return context
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account_login')



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            admin_token = form.cleaned_data.get('admin_token')
            if admin_token == '0ndep1':  # Replace 'your_admin_token_here' with the actual admin token
                user.is_staff = True  # Mark user as staff/admin
            user.save()
            # Log the user in after registration
            login(request, user)
            # Redirect the user to the dashboard
            return redirect('microservice_list')  # Update with the appropriate URL name for the dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})