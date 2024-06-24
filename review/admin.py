from django.contrib import admin
from review.models import review
class reviewAdmin(admin.ModelAdmin):
    list_display=('name','rating','message')
admin.site.register(review,reviewAdmin)
# Register your models here.
