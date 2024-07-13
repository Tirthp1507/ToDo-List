from django.contrib import admin
from django.urls import include, path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    
    path('delete/<int:row_id>/', views.delete_row, name='delete_row'),
]

