from django.contrib import admin

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email', 'photo')
    list_display_links = ('username', 'id')
    search_fields = ('username', 'email')
    ordering = ('id',)
