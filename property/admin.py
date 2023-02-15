from django.contrib import admin

from .models import Flat, Complain, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
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
    inlines = [OwnerInline,]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = (
        'owner_name',
        'owner_pure_phone',
        'owners_phonenumber'
        )

