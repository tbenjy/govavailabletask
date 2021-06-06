from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_organizations_list/', views.get_organizations_list, name='get_organizations_list'),
    path('get_organization_employees/', views.get_organization_employees, name='get_organization_employees'),
    path('get_organization_places/', views.get_organization_places, name='get_organization_places'),
    path('get_employee_ask_history/', views.get_employee_ask_history, name='get_employee_ask_history'),
    path('get_free_places_list/', views.get_free_places_list, name='get_free_places_list'),
]
