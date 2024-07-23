from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.event_index, name='event-index'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('events/<int:event_id>/add_moment/', views.add_moment, name='add-moment'),
    path('assets/create/', views.AssetCreate.as_view(), name='asset-create'),
    path('assets/<int:pk>/', views.AssetDetail.as_view(), name='asset-detail'),
    path('assets/', views.AssetList.as_view(), name='asset-index'),
    path('assets/<int:pk>/update/', views.AssetUpdate.as_view(), name='asset-update'),
    path('assets/<int:pk>/delete/', views.AssetDelete.as_view(), name='asset-delete'),
]