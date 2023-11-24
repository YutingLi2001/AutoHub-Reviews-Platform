from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    """
    CarModelInline allows for direct editing of CarModel instances within CarMake's admin page.
    """
    model = CarModel
    extra = 1  # Reducing the number of extra forms to a reasonable default

class CarModelAdmin(admin.ModelAdmin):
    """
    CarModelAdmin defines the admin interface for CarModel.
    """
    list_display = ('name', 'dealer_id', 'car_type', 'year')  # Use tuples instead of lists for immutability
    list_filter = ('car_type', 'year')  # Quick filter options
    search_fields = ('name', 'dealer_id')  # Allow searching by dealer ID as well
    raw_id_fields = ('make',)  # Use raw_id_fields for ForeignKey to improve performance

class CarMakeAdmin(admin.ModelAdmin):
    """
    CarMakeAdmin defines the admin interface for CarMake.
    """
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)
    # Optionally, add list_filter here if CarMake has fields that would benefit from filtering

# Register models with their respective ModelAdmin
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)  # Register CarMake with CarMakeAdmin to utilize the admin configuration
