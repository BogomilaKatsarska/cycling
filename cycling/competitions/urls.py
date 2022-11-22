from django.urls import path

from cycling.competitions.views import index_competition

urlpatterns = (
    path('', index_competition, name='index competition'),
)
