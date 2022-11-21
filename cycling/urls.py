from django.contrib import admin
from django.urls import path, include

from cycling.cyclist.views import index
from cycling.teams.views import index_teams

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cyclist/', include('cycling.cyclist.urls')),
    path('teams/', index_teams, name='teams'),
)

