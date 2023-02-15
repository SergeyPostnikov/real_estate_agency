from django.contrib import admin

from .models import Flat, Complain, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'new_building')
    readonly_fields = ('created_at',)
    list_display = (
                    'address', 
                    'price', 
                    'new_building', 
                    'construction_year', 
                    'town', 
        )
    list_editable = ('new_building',)
    raw_id_fields = ('liked_by',)


class ComplainAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = (
        'owner_name',
        'owner_pure_phone',
        'owners_phonenumber'
        )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
    