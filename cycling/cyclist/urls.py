from django.urls import path

from cycling.cyclist.views import cyclist_details, cyclists_all

urlpatterns = (
    path('', cyclist_details),
    path('all/', cyclists_all),
)
