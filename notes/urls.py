from django.urls import path

from . import views

urlpatterns = [
    path('', views.Notes.as_view()),
]
