from django.contrib import admin

from cycling.cyclist.models import Cyclist


@admin.register(Cyclist)
class CyclistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country', 'birthday', 'team', 'mail', 'open_for_new_opportunities')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
