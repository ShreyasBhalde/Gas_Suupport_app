from django.contrib import admin
from adminapp.models import customerinfo, servicerequest

@admin.register(servicerequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'request_date', 'details', 'attachment', 'remarks')
    list_filter = ('status', 'request_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'request_type', 'status')
