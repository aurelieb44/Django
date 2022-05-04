from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')), # includes all built in urls
    path('register/', views.register, name='register'), # registration page
]