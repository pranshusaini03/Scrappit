from django.contrib import admin
from service.models import service
class serviceAdmin(admin.ModelAdmin):
    list_display=('name','e_mail','phone_no','subject','message')
admin.site.register(service,serviceAdmin)