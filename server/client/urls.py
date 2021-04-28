from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.index),
    path('<uuid:uuid>/<int:command>/switch', views.switch, name='switch'),
    path('<uuid:uuid>/controlESP', views.controlESP, name='controlESP'),
    path('addClient/', views.addClient, name='addClient'),
    path('delete/', views.delete, name='delete'),
]
