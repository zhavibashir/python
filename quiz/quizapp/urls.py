from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [path('', views.home, name="home"),
path('register/', views.register, name='register'),
path('login/', LoginView.as_view(template_name='quizapp/login.html'), name='login'),
path('logout', LogoutView.as_view(template_name='quizapp/logout.html'), name="logout")]