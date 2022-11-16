from django.urls import path

from cycling.cyclist.views import cyclist_details, cyclists_all, redirect_to_cyclists_comparison_page, show_not_found

urlpatterns = (
    path('<int:pk>/', cyclist_details, name='cyclist details'),
    path('all/', cyclists_all, name='cyclist all'),
    path('redirect/', redirect_to_cyclists_comparison_page),
    path('not-found/', show_not_found, name='show not found'),
)
