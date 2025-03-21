from django.contrib import admin
from .models import TractorBrand, Tractor, TractorImage,TractorVideo

# Register your models here.
@admin.register(TractorBrand)
class TractorBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)  # Filter by active status
    search_fields = ('name',)  # Allow search by brand name
    
@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand__name', 'model_year', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'brand')  # Filter by active status and brand
    search_fields = ('name', 'brand__name')  # Search by tractor name or brand name
    
@admin.register(TractorImage)
class TractorImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'tractor__name', 'tractor__brand__name', 'image', 'created_at', 'updated_at')
    list_filter = ('tractor__brand',)  # Filter by tractor brand

@admin.register(TractorVideo)
class TractorVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tractor__name', 'tractor__brand__name', 'video', 'created_at', 'updated_at')