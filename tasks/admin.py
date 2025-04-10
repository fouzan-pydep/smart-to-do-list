from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# @admin.site.sregister()

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email','password')
    search_fields = ('username', 'first_name', 'last_name', 'email','password')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display=['user','title','description','due_date','importance','estimated_minutes','is_completed','ai_priority_score']

@admin.register(Task_high)
class Task_highadmin(admin.ModelAdmin):
    list_display=['user','title','description','due_date','estimated_minutes','status','repeat_interval']

@admin.register(Task_medium)
class Task_mediumadmin(admin.ModelAdmin):
    list_display=['user','title','description','due_date','estimated_minutes','status','category','importance']

@admin.register(Task_low)
class Task_lowadmin(admin.ModelAdmin):
    list_display=['user','title','description','due_date','importance','estimated_minutes']