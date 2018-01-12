from django.contrib import admin


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'effect')
    list_filter = ['effect', 'type', 'cost']
    ordering = ['name']