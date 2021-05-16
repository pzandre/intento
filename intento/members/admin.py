from django.contrib import admin
from .models import Institute, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'permissions',)


admin.site.register(Institute)
admin.site.register(Profile, ProfileAdmin)
