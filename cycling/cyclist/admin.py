from django.contrib import admin

from cycling.cyclist.models import Cyclist


@admin.register(Cyclist)
class CyclistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'birthday')
