from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('routes/', views.route_list, name='route_list'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('routes/create/', views.route_create, name='route_create'),
    path('routes/<int:route_id>/edit/', views.route_edit, name='route_edit'),
    path('routes/<int:route_id>/delete/', views.route_delete, name='route_delete'),
    path('routes/<int:route_id>/points/', views.point_list, name='point_list'),
    path('routes/<int:route_id>/points/create/', views.point_create, name='point_create'),
    path('points/<int:point_id>/checkin/', views.checkin_create, name='checkin_create'),
]