from django.urls import path
from guide import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-spot/', views.AddSpotView.as_view(), name='add-spot'),
    path('spot-list/', views.SpotListView.as_view(), name='spot-list'),
    path('spot/<int:pk>/', views.SpotView.as_view(), name='spot'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_photo/<int:pk>/', views.AddPhotoView.as_view(), name='add-photo'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]
