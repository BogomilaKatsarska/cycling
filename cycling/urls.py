from django.contrib import admin
from django.urls import path, include

from cycling.cyclist.views import index


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cyclist/', include('cycling.cyclist.urls'), name='cyclist'),
    path('teams/', include('cycling.teams.urls'), name='teams'),
    path('competitions/', include('cycling.competitions.urls'), name='competitions'),
)

