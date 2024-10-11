from django.contrib import admin
from .models import CustomUser, InterestCategory, Interest

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
    )
    search_fields = ('id', 'email')


@admin.register(InterestCategory)
class InterestCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')