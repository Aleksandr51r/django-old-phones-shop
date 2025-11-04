from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    # path('logout', views.Logout.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

]
