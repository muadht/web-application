from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('asset_create/', views.create_asset_view, name='asset_create'),
    path('asset_list/', views.asset_list_view, name='asset_list'),
    path('update/<int:pk>/', views.update_asset_view, name='asset_update'),
    path('asset_delete/<int:pk>/', views.delete_asset_view, name='asset_delete'),
    
    path('create_screen/', views.create_screen_view, name='screen_create'),
    path('screen_list/', views.screen_list_view, name='screen_list'),
    path('update_screen/<int:pk>/', views.update_screen_view, name='screen_update'),
    path('delete_screen/<int:pk>/', views.delete_screen_view, name='screen_delete'),
    
    path('screen_display/<str:screen_path>/', views.screen_display_view, name='screen_display'),

]
