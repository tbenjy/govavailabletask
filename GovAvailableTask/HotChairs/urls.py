from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_organizations_list/', views.get_organizations_list, name='get_organizations_list'),
    path('get_organization_employees/', views.get_organization_employees, name='get_organization_employees'),
    path('get_organization_places/', views.get_organization_places, name='get_organization_places'),
]
