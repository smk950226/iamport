from django.contrib import admin
from .models import Item
from django.utils.safestring import mark_safe

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['img', 'name', 'amount']
    list_display_links = ['img', 'name']

    def img(self, item):
        if item.photo:
            return mark_safe('<img src="{}" style="width: 75px;">'.format(item.photo.url))
        return None