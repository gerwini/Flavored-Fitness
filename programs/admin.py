from django.contrib import admin
from .models import Program

# Register your models here.


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'image',
    )


admin.site.register(Program, ProgramAdmin)
