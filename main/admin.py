from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number', 'bio')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Banner)
admin.site.register(Servise)
admin.site.register(Meal)
admin.site.register(About)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Contacts)
admin.site.register(Info)
admin.site.register(Chef)
admin.site.register(Client)
admin.site.register(Blog_Category)
admin.site.register(Tag)










