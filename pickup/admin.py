from django.contrib import admin
from pickup.models import pickup
class pickupAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_no','address','scrap_type','date','time')
admin.site.register(pickup,pickupAdmin)