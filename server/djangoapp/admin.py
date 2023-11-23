from django.contrib import admin
from .models import CarMake, CarModel

# The following admin classes are used to customize the Django admin interface for our models.

class CarModelInline(admin.StackedInline):
    """
    This inline class allows us to edit `CarModel` objects directly from the `CarMake` admin page.
    """
    model = CarModel
    extra = 1

class CarModelAdmin(admin.ModelAdmin):
    """
    This class provides custom configurations for the `CarModel` admin interface.
    """
    list_display = ('name', 'dealer_id', 'car_type', 'year')  # Use tuples instead of lists for immutability
    search_fields = ('name',)  # Even if there's only one field, make it a tuple for consistency

class CarMakeAdmin(admin.ModelAdmin):
    """
    This class provides custom configurations for the `CarMake` admin interface.
    """
    inlines = [CarModelInline]  # Allows editing of related `CarModel` objects on the same page
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name', 'description')  # Allow searching by name and description

# The `admin.site.register` function is used to register the above configurations with the admin site.

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)  # We should also pass `CarMakeAdmin` to use its configurations

