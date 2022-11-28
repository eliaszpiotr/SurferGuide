from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-spot/', views.AddSpotView.as_view(), name='add-spot'),
    path('spot-list/', views.SpotListView.as_view(), name='spot-list'),
    path('spot/<int:pk>/', views.SpotView.as_view(), name='spot'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('addPhoto/<int:pk>/', views.AddPhoto.as_view(), name='add-photo'),

]
