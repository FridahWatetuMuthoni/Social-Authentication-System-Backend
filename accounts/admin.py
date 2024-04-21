from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','is_staff','age', 'date_of_birth', 'phone_number', 'address', 'gender']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age', 'date_of_birth', 'phone_number', 'address', 'gender',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age', 'date_of_birth', 'phone_number', 'address', 'gender',)}),)

admin.site.register(CustomUser, CustomUserAdmin)