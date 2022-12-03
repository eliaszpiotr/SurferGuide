from django.urls import path
from guide import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.HomeView.as_view(), name='home'),
                  path('add_spot', views.AddSpotView.as_view(), name='add-spot'),
                  path('spot-list/', views.SpotListView.as_view(), name='spot-list'),
                  path('spot/<int:pk>/', views.SpotView.as_view(), name='spot'),
                  path('register/', views.RegisterView.as_view(), name='register'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('logout/', views.LogoutView.as_view(), name='logout'),
                  path('add_photo/<int:pk>/', views.AddPhotoView.as_view(), name='add-photo'),
                  path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
                  path('profile_settings/<int:pk>/', views.ProfileSettingsView.as_view(), name='profile-settings'),
                  path('add_comment/<int:pk>/', views.AddCommentView.as_view(), name='add-comment'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
