from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('close_session/', views.signout, name='close_session')
]
