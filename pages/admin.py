from django.contrib import admin
from .models import Portfolio,Services

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
    list_display_links = ('id','name') #clickable links
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
    list_display_links = ('id','name') #clickable links
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20 #pagination

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Services, ServicesAdmin)