from django.contrib import admin

from .models import Flat, Complain


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'new_building')
    readonly_fields = ('created_at',)
    list_display = (
                    'address', 
                    'price', 
                    'new_building', 
                    'construction_year', 
                    'town', 
                    'owner_pure_phone',
                    'owners_phonenumber'
        )
    list_editable = ('new_building',)
    raw_id_fields = ('liked_by',)


class ComplainAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain)
