from django.urls import path

from . import views

urlpatterns = [
    path('', views.Notes.as_view(), name='note'),
    path('<int:pk>', views.Detail.as_view(), name='detail'),

]