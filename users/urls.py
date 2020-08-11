from django.urls import path

from . import views

urlpatterns = [
    path('signIn', views.SignIn.as_view(), name='signIn'),
    path('signUp', views.SignUp.as_view(), name='signUp'),

]
