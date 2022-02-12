from django.contrib import admin
from.models import list1



class ListAdmin(admin.ModelAdmin):
    list_display = ('name','image')


# Register your models here.
admin.site.register(list1,ListAdmin)