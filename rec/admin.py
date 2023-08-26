from django.contrib import admin

# Register your models here.
from .models import rec

class recAdmin(admin.ModelAdmin):
   list_display=['institute','academic','quota','seattype','gender','openingrank','closingrank','year','round']
admin.site.register(rec,recAdmin)