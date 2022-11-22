from django.urls import path

from cycling.teams.views import index_teams

urlpatterns = (
    path('', index_teams, name='index teams'),
)