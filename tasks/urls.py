from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_task', views.add_task, name='add_task'),
    path('update_task/<int:pk>', views.update_task, name='update_task'),
    path('remove_task/<int:pk>', views.remove_task, name='remove_task'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
