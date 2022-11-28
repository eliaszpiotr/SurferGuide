from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-spot/', views.AddSpotView.as_view(), name='add-spot'),
    path('spot-list/', views.SpotListView.as_view(), name='spot-list'),


]