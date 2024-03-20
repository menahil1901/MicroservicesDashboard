# dashboard/urls.py
from django.urls import path
from .views import DashboardView, MicroserviceListView, MicroserviceCreateView, MicroserviceUpdateView, \
    MicroserviceDeleteView, LogoutView, ServiceDependencyListView, ServiceDependencyCreateView, \
    ServiceDependencyUpdateView, ServiceDependencyDeleteView, UserListView, CreateUserView, \
    UpdateUserView, DeleteUserView, signup_view, ActivityLogListView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('microservices/', MicroserviceListView.as_view(), name='microservice_list'),
    path('microservices/create/', MicroserviceCreateView.as_view(), name='microservice_create'),
    path('microservices/update/<int:pk>/', MicroserviceUpdateView.as_view(), name='microservice_update'),
    path('microservices/delete/<int:pk>/', MicroserviceDeleteView.as_view(), name='microservice_delete'),
    path('service-dependencies/', ServiceDependencyListView.as_view(), name='service_dependency_list'),
    path('service-dependencies/create/', ServiceDependencyCreateView.as_view(), name='service_dependency_create'),
    path('service-dependencies/update/<int:pk>/', ServiceDependencyUpdateView.as_view(), name='service_dependency_update'),
    path('service-dependencies/delete/<int:pk>/', ServiceDependencyDeleteView.as_view(), name='service_dependency_delete'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('activity-logs/', ActivityLogListView.as_view(), name='activity_log_list'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', signup_view, name='signup'),
]
