from django.urls import path
from . import views
app_name = 'view_parkinglots'
urlpatterns = [
    path('', views.index, name='index'),
]