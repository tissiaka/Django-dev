from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('url', 'description', 'https')

# Register your models here.


admin.site.register(Server, ServerAdmin)
