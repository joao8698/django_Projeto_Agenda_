from django.contrib import admin

from contact.models import contact

# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 5
    list_max_show_all = 1000
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',