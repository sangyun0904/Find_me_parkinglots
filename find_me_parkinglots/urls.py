from django.contrib import admin
from django.urls import include, path

app_name = 'view_parkinglots'

urlpatterns = [
    path('view_parkinglots/', include('view_parkinglots.urls')),
    path('admin/', admin.site.urls),
]
