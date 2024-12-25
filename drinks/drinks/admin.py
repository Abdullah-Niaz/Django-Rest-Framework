from django.contrib import admin

from drinks.models import Drink


class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Drink, DrinkAdmin)
