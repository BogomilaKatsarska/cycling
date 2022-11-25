from django.urls import path

from cycling.cyclist.views import cyclist_details, cyclists_all, redirect_to_cyclists_comparison_page, show_not_found, \
    cyclists_open_for_new_opportunities, delete_cyclist

urlpatterns = (
    path('<int:pk>/<slug:slug>/', cyclist_details, name='cyclist details'),
    path('all/', cyclists_all, name='cyclist all'),
    path('redirect/', redirect_to_cyclists_comparison_page),
    path('not-found/', show_not_found, name='show not found'),
    path('opportunities/', cyclists_open_for_new_opportunities, name='opportunities'),
    path('delete/<int:pk>/<slug:slug>/', delete_cyclist, name='delete cyclist'),
)
