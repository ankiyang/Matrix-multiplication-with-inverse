from django.contrib import admin
from models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager","create_timestamp", "last_update_timestamp")
   
admin.site.register(Block,BlockAdmin)
